# Copyright (c) Sunlight Labs, 2012 under the terms and conditions
# of the LICENSE file.

"""
.. module:: sunlight.services.influenceexplorer
    :synopsis: InfluenceExplorer API Implementation

"""

import sunlight.service
import json

service_url = "http://transparencydata.com/api/1.0"

class InfluenceExplorer(sunlight.service.Service):
    """
    """

    def contributions(self, **kwargs):
        return self.get("contributions", **kwargs)

    def lobbying(self, **kwargs):
        return self.get("lobbying", **kwargs)

    def grants(self, **kwargs):
        return self.get("grants", **kwargs)

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
        ret = json.loads( response )
        if "error" in ret:
            ex = InvalidRequestException( ret['error'] )
            ex.response = ret
            raise ex
        return ret

