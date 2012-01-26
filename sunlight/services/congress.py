# Copyright (c) Sunlight Labs, 2012 under the terms and conditions
# of the LICENSE file.

"""
.. module:: sunlight.services.congress
    :synopsis: Sunlight Congress API Implementation

Sunlight Congress API Implementation inside ``python-sunlight``.
"""

import sunlight.service
import json

service_url = "http://services.sunlightlabs.com/api/"

class Congress(sunlight.service.Service):
    """
    Bindings into the `Sunlight Congress <http://services.sunlightlabs.com/docs/Sunlight_Congress_API/>`_
    project. Keep in mind that this is all a very thin wrapper around the API
    it's self, so most of the docuementation is best found on the API doc site
    linked above.
    """

    """
    Get a legislator by a bit of known information. If the query returns more
    then one legislator, this method will throw an error, as is the case with
    the server not finding any information.

    To read more about this, check out the
    `docs <http://services.sunlightlabs.com/docs/congressapi/legislators.get(List)/>`_.
    """
    def legislator( self, **kwargs ):
        return self.get( "legislators.get", **kwargs )

    """
    Get a list of legislators by bits of known information. This method is able
    to return more then one ( a list would be rather lonely without some other
    things in it ), unlike the :func:`sunlight.services.congress.Congress.legislator`
    method.
    """
    def legislators( self, **kwargs ):
        return self.get( "legislators.getList", **kwargs )

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

