#!/usr/bin/env python

import unittest

from geojson_elevation.backends.google import elevation_profile


class TestGoogleBackend(unittest.TestCase):
    """ Google Elevation API tests """
    def test_1_point(self):
        result = elevation_profile('41.889040454306752,12.525333445447737')
        self.assertIn('Point', result['geometry']['type'])
        self.assertEqual(len(result['geometry']['coordinates']), 1)
        self.assertEqual(len(result['geometry']['coordinates'][0]), 3)

    def test_2_points(self):
        result = elevation_profile('41.889040454306752,12.525333445447737|41.889050454306752,12.525335445447737')
        self.assertIn('LineString', result['geometry']['type'])
        self.assertEqual(len(result['geometry']['coordinates']), 2)
        self.assertEqual(len(result['geometry']['coordinates'][0]), 3)
        self.assertEqual(len(result['geometry']['coordinates'][1]), 3)

    def test_elevation_api(self):
        result = elevation_profile('41.889040454306752,12.525333445447737')
        self.assertIn('Point', result['geometry']['type'])
        self.assertEqual(len(result['geometry']['coordinates']), 1)
        self.assertEqual(len(result['geometry']['coordinates'][0]), 3)
        # path, geojson response - LineString
        result = elevation_profile('41.889040454306752,12.525333445447737|41.872041927699982,12.582239191900001', 4)
        self.assertIn('LineString', result['geometry']['type'])
        self.assertEqual(len(result['geometry']['coordinates']), 512)
        self.assertEqual(len(result['geometry']['coordinates'][0]), 3)
        self.assertEqual(len(result['geometry']['coordinates'][-1]), 3)
        # path, geojson response - LineString -automatic sampling
        result = elevation_profile('41.8890404543067518,12.5253334454477372|41.8972185849048984,12.4902286938660296')
        self.assertIn('LineString', result['geometry']['type'])
        self.assertEqual(len(result['geometry']['coordinates']), 72)
        self.assertEqual(len(result['geometry']['coordinates'][0]), 3)
        self.assertEqual(len(result['geometry']['coordinates'][-1]), 3)
