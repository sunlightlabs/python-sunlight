try:
    import unittest2 as unittest
except ImportError:
    import unittest

from sunlight.services.congress import Congress
import sunlight.config
from sunlight.service import EntityDict, EntityList
from sunlight.errors import BadRequestException

class TestCongress(unittest.TestCase):

    def setUp(self):
        self.bioguide_id = 'L000551'
        self.thomas_id = '01501'
        self.ocd_id = 'ocd-division/country:us/state:ca/cd:13'
        self.lat = 35.933333
        self.lon = -79.033333
        self.service = Congress()

    def test_get_badpath(self):
        with self.assertRaises(BadRequestException):
            resp = self.service.get(['foo', 'bar'])

    def test__get_url(self):
        url = self.service._get_url(['bills'],
                                         sunlight.config.API_KEY)

        expected_url = "{base_url}/bills?apikey={apikey}".format(
            base_url='https://congress.api.sunlightfoundation.com',
            apikey=sunlight.config.API_KEY)

        self.assertEqual(url, expected_url)

    def test_pathlist__get_url(self):
        url = self.service._get_url(['legislators', 'locate'],
                                         sunlight.config.API_KEY)

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

    def test_legislator_bad_bioguideid(self):
        results = self.service.legislator('foo')
        self.assertIsNone(results)

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

    def test_locate_districts_by_zip(self):
        results = self.service.locate_districts_by_zip(27514)
        count = results._meta.get('count', None)
        # There is a potential for more than 3 legislators to match on a zipcode
        self.assertNotEqual(len(results), 0)
        self.assertEqual(len(results), count)

    def test_search_bills(self):
        results = self.service.search_bills('Affordable Care Act')
        page = results._meta.get('page', None)
        self.assertIsNotNone(page)
        if page:
            self.assertEqual(page.get('page', None), 1)
            self.assertEqual(page.get('count', None), 20)
        self.assertNotEqual(len(results), 0)

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
