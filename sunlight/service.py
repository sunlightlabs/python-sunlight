# Copyright (c) Sunlight Labs, 2012 under the terms and conditions
# of the LICENSE file.

"""
.. module:: sunlight.service
    :synopsis: Sunlight API Superclass

Base service class. All API classes (such as say -
:class:`sunlight.services.openstates.OpenStates`) inherit from this.
"""
import sys

import sunlight.config
import sunlight.errors

if sys.version_info[0] >= 3:
    from urllib.parse import urlencode
    from urllib.request import urlopen
    from urllib.error import HTTPError
else:
    from urllib import urlencode
    from urllib2 import urlopen
    from urllib2 import HTTPError


class Service:
    """
    Base class for all the API implementations, as well as a bunch of common
    code on how to actually fetch text over the network.
    """

    def get(self, top_level_object, **kwargs):
        """
        Get some data from the network - this is where we actually fetch
        something and make a request.

        .. warning:: Be sure that API_KEY was set before calling this method.
            This will throw a :class:`sunlight.errors.NoAPIKeyException` if
            the API_KEY is not set.

        args:
            ``top_level_object`` (str): Thing to query for (such as say,
                "bills" for OpenStates )

        kwargs:
            These arguments will be passed to the underlying API implementation
            to help create a query. Validation will happen down below, and
            on a per-API level.
        """
        if not sunlight.config.API_KEY:
            raise sunlight.errors.NoAPIKeyException(
"Warning: Missing API Key. please visit " + sunlight.config.API_SIGNUP_PAGE +
" to register for a key.")

        url = self._get_url(top_level_object, sunlight.config.API_KEY,
                            **kwargs)
        try:
            r = urlopen(url)
            return_data = r.read().decode('utf8')
            return self._decode_response(return_data)
        except HTTPError as e:
            message = e.read()
            code = e.getcode()

            ex = sunlight.errors.BadRequestException("Error (%s) -- %s" % (
                code, message
            ))

            ex.url = e.geturl()
            ex.message = message
            ex.code    = code

            raise ex
