# Copyright (c) Sunlight Labs, 2012 under the terms and conditions
# of the LICENSE file.

"""
.. module:: sunlight.services.capitolwords
    :synopsis: CapitolWords API Implementation

CapitolWords API Implementation inside ``python-sunlight``.
"""

from sunlight.errors import InvalidRequestException

import sunlight.service
import json

service_url = "http://capitolwords.org/api"

class CapitolWords(sunlight.service.Service):
    """
    Bindings into the `CapitolWords project <http://capitolwords.org>`_.
    Keep in mind, as you use this wrapper, that this is a very thin translation
    layer from the API into Python. There's no object magic, so the docs on the
    API it's self will be as useful as any of these docstrings.

    Feel free to read up on the CapitolWords API in the
    `docs <http://capitolwords.org/api/>`_.

    If a request goes through and gets a normal response code, but the requested
    action is for whatever reason errorful, a
    :class:`sunlight.errors.InvalidRequestException` will be thrown with the
    error string.
    """

    def dates( self, phrase, **kwargs ):
        """
        Query the CapitolWords server for information regarding the popularity
        of a phrase over a period of time.

        For a list of ``kwargs``, check up on the
        `docs <http://capitolwords.org/api/#dates.json>`_, under
        "Optional arguments"
        """
        kwargs['phrase'] = phrase
        return self.get( "dates", **kwargs )

    def phrases( self, entity_type, entity_value, **kwargs ):
        """
        Query the CapitolWords server for information regarding the top phrases
        for a facet.

        For a list of ``kwargs``, check up on the
        `docs <http://capitolwords.org/api/#phrases.json>`_, under
        "Optional arguments"
        """
        kwargs['entity_type']  = entity_type
        kwargs['entity_value'] = entity_value

        return self.get( "phrases", **kwargs )

    def text( self, **kwargs ):
        """
        Query the CapitolWords server for information regarding 

        For a list of ``kwargs``, check up on the
        `docs <http://capitolwords.org/api/#text.json>`_, under
        "Optional arguments"
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
        ret = json.loads( response )
        if "error" in ret:
            ex = InvalidRequestException( ret['error'] )
            ex.response = ret
            raise ex
        return ret

