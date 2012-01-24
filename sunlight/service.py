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
import sunlight.registry

import urllib2

class Service:
    def __init__(self, service, apikey):
        if service not in sunlight.registry.registered_objects:
            raise sunlight.errors.NoSuchServiceException(
                "Error: No such service: `%s'" % service
            )
        self.service = sunlight.registry.registered_objects[service]()
        self.apikey = apikey

    def get( self, top_level_object, **kwargs ):
        url = self.service.get_url( top_level_object, self.apikey, **kwargs)
        req = urllib2.Request(url)
        try:
            r = urllib2.urlopen(req)
            return_data = r.read()
            return self.service.decode_response( return_data )
        except urllib2.HTTPError as e:
            code = e.getcode()
            raise sunlight.errors.BadRequestException(
                self.service.handle_bad_http_code( code ))
