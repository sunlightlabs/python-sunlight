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
Base service class. This is how we can access most of the goodies from the API
in a single blow.
"""

import sunlight.common
import sunlight.errors

import urllib2

API_KEY = None

class Service:
    def __init__(self):
        if API_KEY == None:
            raise sunlight.errors.NoAPIKeyException(
"Warning: Missing API Key. please visit " + sunlight.common.API_SIGNUP_PAGE +
" to register for a key.")
        self.apikey = API_KEY

    def get( self, top_level_object, **kwargs ):
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
