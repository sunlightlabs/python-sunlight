# Copyright (c) Sunlight Labs, 2012 under the terms and conditions
# of the LICENSE file.

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
