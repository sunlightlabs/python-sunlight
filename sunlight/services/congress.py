# Copyright (c) Sunlight Labs, 2012 under the terms and conditions
# of the LICENSE file.

"""
.. module:: sunlight.services.congress
    :synopsis: Sunlight Congress API Implementation

Sunlight Congress API Implementation inside ``python-sunlight``.
"""

import sunlight.service
import json


API_ROOT = "http://congress.api.sunlightfoundation.com"


class Congress(sunlight.service.Service):
    """
    """

    def legislators(self, **kwargs):
        return self.get('legislators', **kwargs)

    def locate_legislators_by_lat_lon(self, lat, lon, **kwargs):
        kwargs.update({
            "latitude": lat,
            "longitude": lon
        })
        return self.get('legislators/locate', **kwargs)

    def locate_legislators_by_zip(self, zipcode, **kwargs):
        kwargs.update({
            "zip": zipcode
        })
        return self.get('legislators/locate', **kwargs)

    # implementation methods
    def _get_url(self, endpoint, apikey, **kwargs):
        return "%s/%s?apikey=%s&%s" % (
            API_ROOT, endpoint, apikey,
            sunlight.service.safe_encode(kwargs)
        )


    def _decode_response(self, response):
        return json.loads(response)['results']
