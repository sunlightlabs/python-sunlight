# Copyright (C) 2012, Paul Tagliamonte <paultag@sunlightfoundation.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
# of the Software, and to permit persons to whom the Software is furnished to do
# so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
.. module:: sunlight.service
    :platform: Linux, Unix, Windows
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

    def __init__(self):
        """
        Just your basic constructor.

        Raises:
            :class:`sunlight.errors.NoAPIKeyException`

        .. warning::
            Ensure that the API_KEY is set!

        """

        if API_KEY == None:
            raise sunlight.errors.NoAPIKeyException(
"Warning: Missing API Key. please visit " + sunlight.common.API_SIGNUP_PAGE +
" to register for a key.")
        self.apikey = API_KEY

    def get( self, top_level_object, **kwargs ):
        """
        Get some data from the network - this is where we actually fetch
        something and make a request.

        .. warning:: Be sure that API_KEY was set before creating this
            obeject. We really need it right now, and hopefully the __init__
            forced the user into dealing with a lack of key by now.

        args:
            ``top_level_object`` (str): Thing to query for (such as say,
                "bills" for OpenStates )
        
        kwargs:
            These arguments will be passed to the underlying API implementation
            to help create a query. Validation will happen down below, and
            on a per-API level.
        """
        url = self._get_url( top_level_object, self.apikey, **kwargs)
        req = urllib2.Request(url)
        try:
            r = urllib2.urlopen(req)
            return_data = r.read()
            return self._decode_response( return_data )
        except urllib2.HTTPError as e:
            code = e.getcode()
            ex = sunlight.errors.BadRequestException(
                self._handle_bad_http_code( code ))
            ex.url = e.geturl()
            raise ex
