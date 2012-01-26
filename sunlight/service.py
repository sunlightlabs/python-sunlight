# Copyright (c) Sunlight Labs, 2012 under the terms and conditions
# of the LICENSE file.

"""
.. module:: sunlight.service
    :synopsis: Sunlight API Superclass

Base service class. All API classes (such as say -
:class:`sunlight.services.openstates.OpenStates`) inherit from this.
"""

import sunlight.common
import sunlight.errors

import urllib2

API_KEY = None
"""
This might be populated from :func:`sunlight.attempt_to_load_apikey`, or ``Null``
(as it is out of the box). All :class:`sunlight.service.Service` objects will
make use of this API key (once, in it's __init__, not after that) to do their
job.

.. note::
    All Sunlight services share API keys. Nice, right?
"""

class Service:
    """
    Base class for all the API implementations, as well as a bunch of common
    code on how to actually fetch text over the network.
    """

    def get( self, top_level_object, **kwargs ):
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
        if API_KEY == None:
            raise sunlight.errors.NoAPIKeyException(
"Warning: Missing API Key. please visit " + sunlight.common.API_SIGNUP_PAGE +
" to register for a key.")

        url = self._get_url( top_level_object, API_KEY, **kwargs)
        req = urllib2.Request(url)
        try:
            r = urllib2.urlopen(req)
            return_data = r.read()
            return self._decode_response( return_data )
        except urllib2.HTTPError as e:

            message = e.read()
            code = e.getcode()

            ex = sunlight.errors.BadRequestException( "Error (%s) -- %s" % (
                code, message
            ))

            ex.url = e.geturl()
            ex.message = message
            ex.code    = code

            raise ex
