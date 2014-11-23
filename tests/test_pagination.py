try:
    import unittest2 as unittest
except ImportError:
    import unittest

from sunlight.pagination import PagingService
from sunlight.services.congress import Congress
from sunlight.services.opencivic import OpenCivic


class TestPagingService(unittest.TestCase):
    def setUp(self):
        self.congress = Congress()
        self.paginator = PagingService(self.congress)

    def test_non_pageable_service(self):
        """Services that are not pageable should result in an exception being
        raised when instantiating the PagingService.

        """
        with self.assertRaises(ValueError):
            PagingService(OpenCivic())

    def test_paging_past_end(self):
        """Test that requesting a page past the end of the possible results 
        will return a generator of length 0, instead of raising an exception.

        """
        kwargs = {
            'chamber': 'senate',
            'page': 1000
        }
        self.assertEqual(0, len(list(self.paginator.legislators(**kwargs))))

    def test_limit_too_high(self):
        """When setting the limit too high on a request, it should return only
        as many results as exist.

        """
        kwargs = {
            'chamber': 'senate',
            'limit': 101
        }
        self.assertEqual(100, len(list(self.paginator.legislators(**kwargs))))

if __name__ == '__main__':
    unittest.main()
