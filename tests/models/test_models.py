try:
    import unittest2 as unittest
except ImportError:
    import unittest

from sunlight.service import EntityList, EntityDict


class TestEntityList(unittest.TestCase):

    def test_list_meta(self):
        obj = EntityList(['foo', 'bar'], meta={'number': 20})
        self.assertIsNotNone(obj._meta)


class TestEntityDict(unittest.TestCase):

    def test_dict_meta(self):
        obj = EntityDict({'foo' : 'bar'}, meta={'number': 20})
        self.assertIsNotNone(obj._meta)
