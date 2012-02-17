# Copyright (c) Sunlight Labs, 2012 under the terms and conditions
# of the LICENSE file.

"""
.. module:: sunlight.services.influenceexplorer
    :synopsis: InfluenceExplorer API Implementation

InfluenceExplorer API Implementation inside ``python-sunlight``.
"""

from sunlight.errors import InvalidRequestException

import sunlight.service
import json

service_url = "http://transparencydata.com/api/1.0"

class InfluenceExplorer(sunlight.service.Service):
    """
    Bindings into the `InfluenceExplorer <http://influenceexplorer.com/>`_
    project. Be careful to note that this is all a very thing layer over the
    actual API it's self, so be sure to consult the
    `docs <http://data.influenceexplorer.com/api/>`_ when in doubt over a
    method's usage.
    """

    def contributions(self, **kwargs):
        """
        Query the InfluenceExplorer server for information regarding political
        campaign contributions.

        The docs for this method can be found in the
        `docs <http://data.influenceexplorer.com/api/contributions/>`_.
        """
        return self.get("contributions", **kwargs)

    def lobbying(self, **kwargs):
        """
        Query the InfluenceExplorer server for information regarding federal
        lobbying.

        The docs for this method can be found in the
        `docs <http://data.influenceexplorer.com/api/lobbying/>`_
        """
        return self.get("lobbying", **kwargs)

    def grants(self, **kwargs):
        """
        Query the InfluenceExplorer server for information regarding federal
        grants.

        The docs for this method can be found in the
        `docs <http://data.influenceexplorer.com/api/grants/>`_
        """
        return self.get("grants", **kwargs)

    def contracts(self, **kwargs):
        """
        Query the InfluenceExplorer server for information regarding federal
        contracts.

        The docs for this method can be found in the
        `docs <http://data.influenceexplorer.com/api/contracts/>`_
        """
        return self.get("contracts", **kwargs)

    def entities(self, **kwargs):
        """
        Query the InfluenceExplorer server for information regarding aggregate
        contributions by a given entity.

        It sounds much more confusing then it really is.

        The docs for this method can be found in the
        `docs <http://data.influenceexplorer.com/api/aggregates/contributions/>`_
        """
        return self.get("entities", **kwargs)

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

