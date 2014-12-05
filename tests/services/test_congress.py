try:
    import unittest2 as unittest
except ImportError:
    import unittest

import httpretty
import pytest
import json

from sunlight.services.congress import Congress, flatten_dict, preencode_values
import sunlight.config
from sunlight.service import EntityDict
import sunlight.errors


class TestCongressHelpers(unittest.TestCase):

    def test_flatten_dict(self):
        bioguide_id = 'L000551'
        thomas_id = '01501'
        lat = 35.933333
        lon = -79.033333
        nested_dict = {
            'foo': 'bar',
            'legislator': {
                'bioguide_id': bioguide_id,
                'lat': lat,
                'lon': lon,
                'thomas_id': thomas_id
            }
        }
        flat_dict = flatten_dict(nested_dict)

        self.assertIn('legislator.bioguide_id', flat_dict)
        self.assertIn('legislator.lat', flat_dict)
        self.assertIn('legislator.lon', flat_dict)
        self.assertNotIn('legislator', flat_dict)
        self.assertIn('foo', flat_dict)
        self.assertEqual(flat_dict.get('legislator.bioguide_id'), bioguide_id)
        self.assertEqual(flat_dict.get('legislator.lat'), lat)
        self.assertEqual(flat_dict.get('legislator.lon'), lon)
        self.assertEqual(flat_dict.get('foo'), 'bar')

    def test_preencode_values(self):
        unencoded_dict = {
            'foo': False,
            'bar': True,
            'baz': 'false'
        }
        encoded_dict = preencode_values(unencoded_dict)

        self.assertEqual(encoded_dict.get('foo'), 'false')
        self.assertEqual(encoded_dict.get('bar'), 'true')
        self.assertEqual(encoded_dict.get('baz'), 'false')


class TestCongressBase(unittest.TestCase):

    def setUp(self):
        self.bioguide_id = 'L000551'
        self.thomas_id = '01501'
        self.fec_id = 'H8CA09060'
        self.ocd_id = 'ocd-division/country:us/state:ca/cd:13'
        self.lat = 35.933333
        self.lon = -79.033333
        self.zipcode = 27514
        self.bill_id = 'hr3590-111'
        self.service = Congress()


class TestCongress(TestCongressBase):

    def test_get_badpath(self):
        with self.assertRaises(sunlight.errors.BadRequestException):
            self.service.get(['foo', 'bar'])

    def test_get_url(self):
        url = self.service._get_url(['bills'], sunlight.config.API_KEY)

        expected_url = "{base_url}/bills?apikey={apikey}".format(
            base_url='https://congress.api.sunlightfoundation.com',
            apikey=sunlight.config.API_KEY)

        self.assertEqual(url, expected_url)

    def test_http_vs_https(self):
        service = Congress(use_https=False)

        http_url = service._get_url(['bills'], sunlight.config.API_KEY)
        expected_url = "{base_url}/bills?apikey={apikey}".format(
            base_url='http://congress.api.sunlightfoundation.com',
            apikey=sunlight.config.API_KEY)

        self.assertEqual(http_url, expected_url)

        service.use_https = True
        url = service._get_url(['bills'], sunlight.config.API_KEY)
        expected_url = "{base_url}/bills?apikey={apikey}".format(
            base_url='https://congress.api.sunlightfoundation.com',
            apikey=sunlight.config.API_KEY)

        self.assertEqual(url, expected_url)

    def test_pathlist__get_url(self):
        url = self.service._get_url(['legislators', 'locate'], sunlight.config.API_KEY)

        expected_url = "{base_url}/legislators/locate?apikey={apikey}".format(
            base_url='https://congress.api.sunlightfoundation.com',
            apikey=sunlight.config.API_KEY)

        self.assertEqual(url, expected_url)

    def test_legislator(self):
        results = self.service.legislator(self.bioguide_id)
        self.assertIsNotNone(results)
        page = results._meta.get('page', None)
        self.assertIsNotNone(page)
        if page:
            self.assertEqual(page.get('page', None), 1)
            self.assertEqual(page.get('count', None), 1)
        self.assertIsInstance(results, EntityDict)

    def test_legislator_thomas_id(self):
        results = self.service.legislator(self.thomas_id, id_type='thomas')
        self.assertIsNotNone(results)
        page = results._meta.get('page', None)
        self.assertIsNotNone(page)
        if page:
            self.assertEqual(page.get('page', None), 1)
            self.assertEqual(page.get('count', None), 1)
        self.assertIsInstance(results, EntityDict)

    def test_legislator_ocd_id(self):
        results = self.service.legislator(self.ocd_id, id_type='ocd')
        self.assertIsNotNone(results)
        page = results._meta.get('page', None)
        self.assertIsNotNone(page)
        if page:
            self.assertEqual(page.get('page', None), 1)
            self.assertEqual(page.get('count', None), 1)
        self.assertIsInstance(results, EntityDict)

    def test_legislator_fec_id(self):
        results = self.service.legislator(self.fec_id, id_type='fec')
        self.assertIsNotNone(results)
        page = results._meta.get('page', None)
        self.assertIsNotNone(page)
        if page:
            self.assertEqual(page.get('page', None), 1)
            self.assertEqual(page.get('count', None), 1)
        self.assertIsInstance(results, EntityDict)

    def test_legislator_bad_bioguideid(self):
        results = self.service.legislator('foo')
        self.assertIsNone(results)

    def test_legislator_bioguide_id_incorrect_type(self):
        results = self.service.legislator(self.bioguide_id, id_type='krampus')
        self.assertIsNotNone(results)
        page = results._meta.get('page', None)
        self.assertIsNotNone(page)
        if page:
            self.assertEqual(page.get('page', None), 1)
            self.assertEqual(page.get('count', None), 1)
        self.assertIsInstance(results, EntityDict)

    def test_legislators(self):
        results = self.service.legislators()
        page = results._meta.get('page', None)
        self.assertIsNotNone(page)
        if page:
            self.assertEqual(page.get('page', None), 1)
            self.assertEqual(page.get('count', None), 20)
        self.assertNotEqual(len(results), 0)

    def test_all_legislators_in_office(self):
        results = self.service.all_legislators_in_office()
        page = results._meta.get('page', None)
        self.assertIsNotNone(page)
        if page:
            # In this case, page should be None
            self.assertEqual(page.get('page', 0), None)
            # Should be more then 20, but I don't want to compare to 538, do I?
            self.assertGreater(page.get('count', None), 100)
        self.assertNotEqual(len(results), 0)

    def test_locate_legislators_by_lat_lon(self):
        results = self.service.locate_legislators_by_lat_lon(self.lat, self.lon)
        count = results._meta.get('count', None)
        # For a state, there should be 2 senators and 1 representative.
        self.assertEqual(len(results), 3)
        self.assertEqual(len(results), count)

    def test_locate_legislators_by_zip(self):
        results = self.service.locate_legislators_by_zip(self.zipcode)
        count = results._meta.get('count', None)
        # A zipcode may overlap multiple districts, so can return more then 3 results
        self.assertGreaterEqual(len(results), 3)
        self.assertEqual(len(results), count)

    def test_locate_districts_by_zip(self):
        results = self.service.locate_districts_by_zip(self.zipcode)
        count = results._meta.get('count', None)
        # There is a potential for more than 3 legislators to match on a zipcode
        self.assertNotEqual(len(results), 0)
        self.assertEqual(len(results), count)

    def test_locate_districts_by_lat_lon(self):
        results = self.service.locate_districts_by_lat_lon(self.lat, self.lon)
        count = results._meta.get('count', None)
        # We should get 1 and only one district for a lat/lon
        self.assertEqual(len(results), 1)
        self.assertEqual(len(results), count)

    def test_bills(self):
        results = self.service.bills(congress=113, history={'enacted': True},
                                     bill_type__in='hjres|sjres')
        page = results._meta.get('page', None)
        self.assertIsNotNone(page)
        if page:
            self.assertEqual(page.get('page', None), 1)
            self.assertLessEqual(page.get('count', None), 20)
        self.assertNotEqual(len(results), 0)

    def test_bill_by_id(self):
        result = self.service.bill(self.bill_id)
        page = result._meta.get('page', None)
        self.assertIsNotNone(page)
        if page:
            self.assertEqual(page.get('page', None), 1)
            self.assertEqual(page.get('count', None), 1)
        self.assertEqual(result._meta.get('count', None), 1)
        self.assertNotEqual(len(result), 1)
        self.assertIsNotNone(result.get('introduced_on'))
        self.assertIsNotNone(result.get('number'))

    def test_bill_using_bad_id(self):
        result = self.service.bill('abadbillid')
        self.assertIsNone(result)

    def test_search_bills(self):
        results = self.service.search_bills('Affordable Care Act')
        page = results._meta.get('page', None)
        self.assertIsNotNone(page)
        if page:
            self.assertEqual(page.get('page', None), 1)
            self.assertEqual(page.get('count', None), 20)
        self.assertNotEqual(len(results), 0)

    def test_upcoming_bills(self):
        results = self.service.upcoming_bills()
        self.assertIsNotNone(results)
        page = results._meta.get('page', None)
        if page:
            self.assertEqual(page.get('page', None), 1)
            self.assertEqual(page.get('count', None), 20)

    def test_committees(self):
        results = self.service.committees()
        page = results._meta.get('page', None)
        self.assertIsNotNone(page)
        if page:
            self.assertEqual(page.get('page', None), 1)
            self.assertEqual(page.get('count', None), 20)
        self.assertNotEqual(len(results), 0)

    def test_amendments(self):
        results = self.service.amendments()
        page = results._meta.get('page', None)
        self.assertIsNotNone(page)
        if page:
            self.assertEqual(page.get('page', None), 1)
            self.assertEqual(page.get('count', None), 20)
        self.assertNotEqual(len(results), 0)

    def test_votes(self):
        results = self.service.votes()
        page = results._meta.get('page', None)
        self.assertIsNotNone(page)
        if page:
            self.assertEqual(page.get('page', None), 1)
            self.assertEqual(page.get('count', None), 20)
        self.assertNotEqual(len(results), 0)

    def test_floor_updates(self):
        results = self.service.floor_updates()
        page = results._meta.get('page', None)
        self.assertIsNotNone(page)
        if page:
            self.assertEqual(page.get('page', None), 1)
            self.assertEqual(page.get('count', None), 20)
        self.assertNotEqual(len(results), 0)

    def test_hearings(self):
        results = self.service.hearings()
        page = results._meta.get('page', None)
        self.assertIsNotNone(page)
        if page:
            self.assertEqual(page.get('page', None), 1)
            self.assertEqual(page.get('count', None), 20)
        self.assertNotEqual(len(results), 0)

    def test_nominations(self):
        results = self.service.nominations()
        page = results._meta.get('page', None)
        self.assertIsNotNone(page)
        if page:
            self.assertEqual(page.get('page', None), 1)
            self.assertEqual(page.get('count', None), 20)
        self.assertNotEqual(len(results), 0)

    def test_documents(self):
        results = self.service.documents()
        page = results._meta.get('page', None)
        self.assertIsNotNone(page)
        if page:
            self.assertEqual(page.get('page', None), 1)
            self.assertEqual(page.get('count', None), 20)
        self.assertNotEqual(len(results), 0)

    def test_documents_gao_reports(self):
        results = self.service.documents(document_type='gao_report')
        page = results._meta.get('page', None)
        self.assertIsNotNone(page)
        if len(results):
            for item in results:
                self.assertIsInstance(item, dict)
                self.assertEqual(item.get('document_type', None), 'gao_report')
        self.assertNotEqual(len(results), 0)

    def test_documents_ig_reports(self):
        results = self.service.documents(document_type='ig_report')
        page = results._meta.get('page', None)
        self.assertIsNotNone(page)
        if len(results):
            for item in results:
                self.assertIsInstance(item, dict)
                self.assertEqual(item.get('document_type', None), 'ig_report')
        self.assertNotEqual(len(results), 0)

    def test_congressional_documents(self):
        results = self.service.congressional_documents()
        page = results._meta.get('page', None)
        self.assertIsNotNone(page)
        if page:
            self.assertEqual(page.get('page', None), 1)
            self.assertEqual(page.get('count', None), 20)
        self.assertNotEqual(len(results), 0)


# class TestCongressWithMocks(TestCongressBase):

#     @classmethod
#     def tearDownClass(cls):
#         httpretty.disable()  # disable after local tests are done.
#         httpretty.reset()    # reset HTTPretty state (clean up registered urls and request history)

#     @pytest.mark.httpretty
#     def test_malformed_response(self):
#         httpretty.register_uri(httpretty.GET,
#                                'https://congress.api.sunlightfoundation.com/legislators',
#                                body='This is a bad response body',)

#         with self.assertRaises(sunlight.errors.SunlightException):
#             self.service.legislators()

#     @pytest.mark.httpretty
#     def test_error_exception(self):
#         httpretty.register_uri(httpretty.GET,
#                                'https://congress.api.sunlightfoundation.com/legislators',
#                                body='500 Server Error',
#                                status=500)

#         with self.assertRaises(sunlight.errors.BadRequestException):
#             self.service.legislators()

#     @pytest.mark.httpretty
#     def test_response_parse(self):
#         response = {
#             "results": [{"foo": "bar"}],
#             "count": 919,
#             "page": {
#                 "count": 20,
#                 "per_page": 20,
#                 "page": 1
#             }
#         }
#         response_string = json.dumps(response)

#         httpretty.register_uri(httpretty.GET,
#                                'https://congress.api.sunlightfoundation.com/legislators',
#                                body=response_string)

#         results = self.service.legislators()

#         self.assertIsInstance(results, list)
#         self.assertEqual(len(results), 1)

#         self.assertIsNotNone(results._meta)
#         self.assertIsInstance(results._meta, dict)
#         self.assertEqual(results._meta.get('count', None), 919)

#         page = results._meta.get('page', None)
#         self.assertIsInstance(page, dict)
#         self.assertEqual(page.get('count'), 20)
#         self.assertEqual(page.get('per_page'), 20)
#         self.assertEqual(page.get('page'), 1)
