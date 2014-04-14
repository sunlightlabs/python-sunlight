try:
    import unittest2 as unittest
except ImportError:
    import unittest

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
        url = self.service._get_url(['phrases'],
                                             sunlight.config.API_KEY,
                                             **self.phrases_kwargs)

        expected_url = '{base_url}/phrases.json?apikey={apikey}&{args}'.format(
            base_url='http://capitolwords.org/api/1',
            apikey=sunlight.config.API_KEY,
            args=sunlight.service.safe_encode(self.phrases_kwargs)).strip('&')

        self.assertEqual(url, expected_url)

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
