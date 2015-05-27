try:
    import unittest2 as unittest
except ImportError:
    import unittest

import random

from sunlight.services.openstates import Openstates
import sunlight.config
from sunlight.errors import BadRequestException

class TestOpenStates(unittest.TestCase):

    def setUp(self):
        self.service = Openstates()
        self.a_state_abbreviation = 'nc'
        self.a_bill_id = 'NCB00007259'
        self.a_bill_official_id = 'HB 786'
        self.expected_metadata_keys = ('name', 'abbreviation', 'chambers', 'feature_flags')
        self.lat = 35.933333
        self.lon = -79.033333
        self.a_committee_id = 'NCC000169'
        self.a_state_with_events = 'tx'
        self.an_event_id = 'TXE00026474'
        self.a_boundary_id = 'ocd-division/country:us/state:nc/sldl:1'

    def test_bad__get_url(self):
        with self.assertRaises(BadRequestException):
            self.service._get_url(['districts', None], sunlight.config.API_KEY)

    def test_all_metadata(self):
        all_metadata = self.service.all_metadata()
        random_metadata = random.choice(all_metadata)
        for expected_key in self.expected_metadata_keys:
            self.assertIn(expected_key, random_metadata)
        self.assertGreaterEqual(len(all_metadata), 50)

    def test_state_metadata(self):
        state_metadata = self.service.state_metadata(self.a_state_abbreviation)
        for expected_key in self.expected_metadata_keys:
            self.assertIn(expected_key, state_metadata)
        self.assertEqual(state_metadata.get('abbreviation'), self.a_state_abbreviation)

    def test_bill_search(self):
        num_results = 20
        page_num = 1
        results = self.service.bills(state=self.a_state_abbreviation, per_page=num_results, page=page_num)
        self.assertLessEqual(len(results), num_results)

    def test_get_bill(self):
        result = self.service.bill(self.a_bill_id)
        self.assertEqual(result.get('state'), self.a_state_abbreviation)
        self.assertEqual(result.get('bill_id'), self.a_bill_official_id)

    def test_bill_detail(self):
        result = self.service.bill_detail('nc', '2013', self.a_bill_official_id)
        self.assertEqual(result.get('state'), self.a_state_abbreviation)
        self.assertEqual(result.get('bill_id'), self.a_bill_official_id)

    def test_bill_detail_with_session_int(self):
        result = self.service.bill_detail('nc', 2013, self.a_bill_official_id)
        self.assertEqual(result.get('state'), self.a_state_abbreviation)
        self.assertEqual(result.get('bill_id'), self.a_bill_official_id)

    def test_bill_detail_with_chamber(self):
        result = self.service.bill_detail('nc', '2013', self.a_bill_official_id, 'lower')
        self.assertEqual(result.get('state'), self.a_state_abbreviation)
        self.assertEqual(result.get('bill_id'), self.a_bill_official_id)

    def test_legislators_search_by_last_name(self):
        last_name = 'Smith'
        results = self.service.legislators(last_name=last_name)
        for item in results:
            self.assertEqual(item.get('last_name'), last_name)

    def test_legislator_detail(self):
        leg_id = 'MDL000210'
        result = self.service.legislator_detail(leg_id)
        self.assertEqual(result.get('leg_id'), leg_id)

    def test_legislator_geo_search(self):
        results = self.service.legislator_geo_search(self.lat, self.lon)
        self.assertGreaterEqual(len(results), 1) # Derp. I don't know.
        for item in results:
            self.assertTrue(item.get('active'))
            self.assertEqual(item.get('state'), self.a_state_abbreviation)

    def test_committees_search(self):
        results = self.service.committees(state=self.a_state_abbreviation)
        self.assertGreaterEqual(len(results), 1) # Derp. I don't know.
        for item in results:
            self.assertEqual(item.get('state'), self.a_state_abbreviation)
            self.assertIsNotNone(item.get('committee'))

    def test_committee_detail(self):
        result = self.service.committee_detail(self.a_committee_id)
        self.assertEqual(result.get('id'), self.a_committee_id)
        self.assertIsNotNone(result.get('committee'))

    def test_events_search(self):
        results = self.service.events(state=self.a_state_with_events)
        for item in results:
            self.assertIsNotNone(item.get('id'))
            self.assertEqual(item.get('state'), self.a_state_with_events)

    def test_event_detail(self):
        item = self.service.event_detail(self.an_event_id)
        self.assertIsNotNone(item.get('id'))
        self.assertEqual(item.get('state'), self.a_state_with_events)

    def test_districts_search(self):
        results = self.service.districts(self.a_state_abbreviation, 'upper')
        for item in results:
            self.assertIsNotNone(item.get('id'))
            self.assertIsNotNone(item.get('name'))
            self.assertEqual(item.get('abbr'), self.a_state_abbreviation)

    def test_districts_boundary(self):
        item = self.service.district_boundary(self.a_boundary_id)
        self.assertIsNotNone(item.get('id'))
        self.assertIsNotNone(item.get('name'))
        self.assertIsNotNone(item.get('bbox'))
        self.assertIsNotNone(item.get('chamber'))
        self.assertIsNotNone(item.get('num_seats'))
        self.assertIsNotNone(item.get('region'))
        self.assertIsNotNone(item.get('shape'))
        self.assertEqual(item.get('boundary_id'), self.a_boundary_id)
