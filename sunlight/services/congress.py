# Copyright (c) Sunlight Labs, 2012 under the terms and conditions
# of the LICENSE file.

"""
.. module:: sunlight.services.congress
    :synopsis: Sunlight Congress API Implementation

Sunlight Congress API Implementation inside ``python-sunlight``.
"""

import sunlight.service
import json


class Congress(sunlight.service.Service):
    """
    Bindings into the `Sunlight Congress API
    <http://services.sunlightlabs.com/docs/Sunlight_Congress_API/>`_, an API
    primarily for details on current federal legislators.
    """

    # implementation methods
    def _get_url(self, obj, apikey, **kwargs):
        return "%s/%s?apikey=%s&%s" % (
            service_url,
            obj,
            apikey,
            sunlight.service.safe_encode(kwargs)
        )
