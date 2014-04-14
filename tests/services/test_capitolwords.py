try:
    import unittest2 as unittest
except ImportError:
    import unittest

try:
    from urllib.parse import urlparse, parse_qsl
except ImportError:
    from urlparse import urlparse, parse_qsl

from sunlight.services.capitolwords import CapitolWords
import sunlight.config
from sunlight.service import EntityDict, EntityList
from sunlight.errors import BadRequestException


class TestCapitolWords(unittest.TestCase):

    def setUp(self):
        self.phrases_kwargs = {
            'entity_type': 'legislator',
            'entity_value':  'L000551'
        }
        self.service = CapitolWords()

    def test__get_url(self):
        '''This is probably a bad idea and should be replaced.'''
        url = self.service._get_url(['phrases'],
                                             sunlight.config.API_KEY,
                                             **self.phrases_kwargs)

        expected_hostname = 'capitolwords.org'
        expected_path = '/api/1/phrases.json'
        expected_query = {
            'apikey': sunlight.config.API_KEY
        }
        expected_query.update(self.phrases_kwargs)

        parsed_url = urlparse(url)
        parsed_query = dict(parse_qsl(parsed_url.query))

        self.assertEqual(parsed_url.hostname, expected_hostname)
        self.assertEqual(parsed_url.path, expected_path)
        self.assertDictEqual(parsed_query, expected_query)

    def test_dates(self):
        results = self.service.dates('Obamacare')
        self.assertNotEqual(len(results), 0)

    def test_phrases_by_entity(self):
        results = self.service.phrases_by_entity('state',
                                                          phrase='Obamacare')
        self.assertNotEqual(len(results), 0)

    def test_legislator_phrases(self):
        results = self.service.phrases(
            self.phrases_kwargs['entity_type'],
            self.phrases_kwargs['entity_value'])

        self.assertNotEqual(len(results), 0)

    def test_text(self):
        results = self.service.text('Christmas')
        self.assertNotEqual(len(results), 0)
