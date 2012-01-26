# Copyright (c) Sunlight Labs, 2012 under the terms and conditions
# of the LICENSE file.

"""
.. module:: sunlight.services.congress
    :synopsis: Sunlight Congress API Implementation

Sunlight Congress API Implementation inside ``python-sunlight``.
"""

import sunlight.service
import urllib
import json

service_url = "http://services.sunlightlabs.com/api/"

def _unpack_legislators(resp):
    return [e['legislator'] for e in resp['legislators']]
def _unpack_districts(resp):
    return [e['district'] for e in resp['districts']]
def _unpack_committees(resp):
    return [e['committee'] for e in resp['committees']]

class Congress(sunlight.service.Service):
    """
    Bindings into the `Sunlight Congress <http://services.sunlightlabs.com/docs/Sunlight_Congress_API/>`_.
    """

    def legislators(self, **kwargs):
        """
        Query the Congress API for all legislators matching certain criteria.

        See documentation at `legislators.get(List)
        <http://services.sunlightlabs.com/docs/congressapi/legislators.get(List)/>`_
        """
        return _unpack_legislators(self.get('legislators.getList', **kwargs))


    def legislators_for_zip(self, zipcode):
        """
        Query the Congress API for all legislators representing a given ZIP
        code.

        This method is not recommended, prefer legislators_for_lat_lon instead.
        See the blog post `"Don't Use Zip Codes Unless You Have To"
        <http://sunlightlabs.com/blog/2012/dont-use-zipcodes/>`_.

        See documentation at `legislators.allForZip
        <http://services.sunlightlabs.com/docs/congressapi/legislators.allForZip/>`_
        """
        return _unpack_legislators(self.get('legislators.allForZip',
                                            zip=zipcode))

    def legislators_for_lat_lon(self, latitude, longitude):
        """
        Query the Congress API for all legislators representing an given
        location.

        See documentation at `legislators.allForLatLong
        <http://services.sunlightlabs.com/docs/congressapi/legislators.allForLatLong/>`_
        """
        return _unpack_legislators(self.get('legislators.allForLatLong',
                                            latitude=latitude,
                                            longitude=longitude))

    def districts_for_zip(self, zipcode):
        """
        Query the Congress API for all congressional districts overlapping a
        zip code.

        See documentation at `districts.getDistrictFromLatLong
        <http://services.sunlightlabs.com/docs/congressapi/districts.getDistrictFromLatLong/>`_
        """
        return _unpack_districts(self.get('districts.getDistrictsFromZip',
                                            zip=zipcode))

    def districts_for_lat_long(self, latitude, longitude):
        """
        Query the Congress API for all congressional districts containing a
        given location.

        See documentation at `districts.getDistrictFromLatLong
        <http://services.sunlightlabs.com/docs/congressapi/districts.getDistrictFromLatLong/>`_
        """
        return _unpack_districts(self.get('districts.getDistrictFromLatLong',
                                            latitude=latitude,
                                            longitude=longitude))

    def committees(self, chamber):
        """
        Query the Congress API for all committees for a chamber.
        (House|Senate|Joint)

        See documentation at `committees.getList
        <http://services.sunlightlabs.com/docs/congressapi/committees.getList/>`_
        """
        return _unpack_committees(self.get('committees.getList',
                                           chamber=chamber))

    def committee_detail(self, id):
        """
        Query the Congress API for all details for a committee, including
        members.

        See documentation at `committees.get
        <http://services.sunlightlabs.com/docs/congressapi/committees.get/>`_
        """
        return self.get('committees.get', id=id)['committee']

    def committees_for_legislator(self, bioguide_id):
        """
        Query the Congress API for all details for a committee, including
        members.

        See documentation at `committees.allForLegislator
        <http://services.sunlightlabs.com/docs/congressapi/committees.allForLegislator/>`_
        """
        return _unpack_committees(self.get('committees.allForLegislator',
                                           bioguide_id=bioguide_id))

    # implementation methods
    def _get_url(self, obj, apikey, **kwargs):
        return "%s/%s?apikey=%s&%s" % (
            service_url,
            obj,
            apikey,
            urllib.urlencode(kwargs.items())
        )

    def _decode_response(self, response):
        return json.loads(response)['response']
