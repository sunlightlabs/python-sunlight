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
    """
    Bindings into the CapitolWords project

    API Ref:            http://capitolwords.org/api/
    About the project:  http://capitolwords.org/api/
    """

    def dates( self, **kwargs ):
        """
        Find the popularity of a phrase over a period of time.
        Standard arguments are supported.
        """
        return self.get( "dates", **kwargs )

    def phrases( self, **kwargs ):
        """
        List the top phrases for a facet.
        """
        return self.get( "phrases", **kwargs )

    def text( self, **kwargs ):
        """
        Full-text search. Standard arguments are supported
        """
        return self.get( "text", **kwargs )

    # API impl methods below

    def _get_url( self, obj, apikey, **kwargs ):
        ret = "%s/%s.json?apikey=%s" % (
            service_url,
            obj,
            apikey
        )
        for arg in kwargs:
            ret += "&%s=%s" % ( arg, kwargs[arg] )
        return ret

    def _decode_response( self, response ):
        return json.loads( response )

    def _handle_bad_http_code( self, code ):
        # Soon to be deprecated
        messages = {}
        try:
            return messages[code]
        except KeyError as e:
            return "Unknown error code!!! Recieved a %s from the server." % (
                str( code )
            )
