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

import sunlight.service

import json

module_name = "capitolwords"
service_url = "http://capitolwords.org/api"

class CapitolWords(sunlight.service.Service):

    def dates( self, **kwargs ):
        return self.get( "dates", **kwargs )

    def phrases( self, **kwargs ):
        return self.get( "phrases", **kwargs )

    def text( self, **kwargs ):
        return self.get( "text", **kwargs )

    def get_url( self, obj, apikey, **kwargs ):
        ret = "%s/%s.json?apikey=%s" % (
            service_url,
            obj,
            apikey
        )
        for arg in kwargs:
            ret += "&%s=%s" % ( arg, kwargs[arg] )
        return ret

    def decode_response( self, response ):
        return json.loads( response )

    def handle_bad_http_code( self, code ):
        messages = {}
        try:
            return messages[code]
        except KeyError as e:
            return "Unknown error code!!! Recieved a %s from the server." % (
                str( code )
            )
