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

LEGISLATOR_ID_TYPES = (
    'bioguide',
    'thomas',
    'lis',
    'govtrack',
    'votesmart',
    'crp',
    'fec',
)


class Congress(sunlight.service.Service):
    """
    Bindings to the `Congress API <http://sunlightlabs.github.io/congress/>`_.
    Keep in mind this is a thin wrapper around the API so the API documentation
    is the place to look for help on field names and examples.
    """

    def legislators(self, **kwargs):
        """
        Search and filter for members of Congress.

        For details see `Legislators API docs
        <http://sunlightlabs.github.io/congress/legislators.html>`
        """
        return self.get('legislators', **kwargs)

    def legislator(self, identifier, id_type=LEGISLATOR_ID_TYPES[0], **kwargs):
        """
        Retrieve a member of Congress by a unique identifier. Defaults to
        bioguide. Choices are:

            * bioguide
            * thomas
            * lis
            * govtrack
            * votesmart
            * crp
            * fec

        For details see `Legislators API docs
        <http://sunlightlabs.github.io/congress/legislators.html>`
        """
        if id_type not in LEGISLATOR_ID_TYPES:
            id_type = LEGISLATOR_ID_TYPES[0]
        id_arg = {}
        if id_type == 'fec':
            id_arg['fec_ids'] = identifier
        else:
            id_key = '{0}_id'.format(id_type)
            id_arg[id_key] = identifier

        kwargs.update(id_arg)
        results = self.get('legislators', **kwargs)
        if len(results):
            return results[0]
        return None


    def all_legislators_in_office(self, **kwargs):
        """
        Returns all legislators currently in office (non-paginated response).

        For details see `Legislators API docs
        <http://sunlightlabs.github.io/congress/legislators.html>`
        """
        kwargs.update({
            "per_page": "all"
        })
        return self.get('legislators', **kwargs)

    def locate_legislators_by_lat_lon(self, lat, lon, **kwargs):
        """
        Find members of Congress by a latitude and longitude.

        For details see `Legislators API docs
        <http://sunlightlabs.github.io/congress/legislators.html#methods/legislators-locate>`
        """
        kwargs.update({
            "latitude": lat,
            "longitude": lon
        })
        return self.get('legislators/locate', **kwargs)

    def locate_legislators_by_zip(self, zipcode, **kwargs):
        """
        Find members of Congress by zip code.

        For details see `Legislators API docs
        <http://sunlightlabs.github.io/congress/legislators.html#methods/legislators-locate>`
        """
        kwargs.update({
            "zip": zipcode
        })
        return self.get('legislators/locate', **kwargs)

    def bills(self, **kwargs):
        """
        Search and filter through bills in Congress.

        For details see `Bills API docs
        <http://sunlightlabs.github.io/congress/bills.html>`
        """
        return self.get('bills', **kwargs)

    def bill(self, bill_id, **kwargs):
        """
        Retrieve a bill by bill_id.

        For details see `Bills API docs
        <http://sunlightlabs.github.io/congress/bills.html>`
        """
        kwargs.update({
            "bill_id": bill_id
        })
        results = self.get('bills', **kwargs)
        if len(results):
            return results[0]
        return None

    def search_bills(self, query, **kwargs):
        """
        Search the full text of legislation, and other fields.

        For details see `Bills API docs
        <http://sunlightlabs.github.io/congress/bills.html#methods/bills-search>`
        """
        kwargs.update({
            "query": query
        })
        return self.get('bills/search', **kwargs)

    def upcoming_bills(self, **kwargs):
        """
        Search and filter through upcoming bills in the House and Senate.

        This will return bills that have been scheduled by
        party leadership for upcoming House and Senate floor action.

        For details see `Upcoming Bills API docs
        <http://sunlightlabs.github.io/congress/upcoming_bills.html>`
        """
        return self.get('upcoming_bills', **kwargs)

    def locate_districts_by_lat_lon(self, lat, lon, **kwargs):
        """
        Find congressional districts by a latitude and longitude.

        For details see `Districts API docs
        <http://sunlightlabs.github.io/congress/districts.html>`
        """
        kwargs.update({
            "latitude": lat,
            "longitude": lon
        })
        return self.get('/districts/locate', **kwargs)

    def locate_districts_by_zip(self, zipcode, **kwargs):
        """
        Find congressional districts by a latitude and longitude.

        For details see `Districts API docs
        <http://sunlightlabs.github.io/congress/districts.html>`
        """
        kwargs.update({
            "zip": zipcode,
        })
        return self.get('/districts/locate', **kwargs)

    def committees(self, **kwargs):
        """
        Search and filter through committees in the House and Senate.

        For details see `Bill API docs
        <http://sunlightlabs.github.io/congress/committees.html>`
        """
        return self.get('committees', **kwargs)

    def amendments(self, **kwargs):
        """
        Search and filter through committees in Congress.

        For details see `Amendments API docs
        <http://sunlightlabs.github.io/congress/committees.html>`
        """
        return self.get('amendments', **kwargs)

    def votes(self, **kwargs):
        """
        Search and filter through votes in Congress.

        For details see `Votes API docs
        <http://sunlightlabs.github.io/congress/votes.html>`
        """
        return self.get('votes', **kwargs)

    def floor_updates(self, **kwargs):
        """
        Search and filter through floor updates in the House and Senate.

        For details see `Floor Updates API docs
        <http://sunlightlabs.github.io/congress/floor_updates.html>`
        """
        return self.get('floor_updates', **kwargs)

    def hearings(self, **kwargs):
        """
        Search and filter through committee hearings in the House and Senate.

        For details see `Hearings API docs
        <http://sunlightlabs.github.io/congress/hearings.html>`
        """
        return self.get('hearings', **kwargs)

    # implementation methods
    def _get_url(self, endpoint, apikey, **kwargs):
        return "%s/%s?apikey=%s&%s" % (
            API_ROOT, endpoint, apikey,
            sunlight.service.safe_encode(kwargs)
        )

    def _decode_response(self, response):
        return json.loads(response)['results']
