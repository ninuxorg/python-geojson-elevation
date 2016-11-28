import os
import responses
import unittest

from geojson_elevation.backends.google import elevation
from geojson_elevation.exceptions import ElevationApiError


class TestGoogleBackend(unittest.TestCase):

    def load_fixture(self, file):
        return open(os.path.abspath(file)).read()

    """ Google Elevation API tests """
    @responses.activate
    def test_1_point(self):
        responses.add(
            responses.GET,
            "https://maps.googleapis.com/maps/api/elevation/json?locations=41.889040454306752%2C12.525333445447737",
            body=self.load_fixture("tests/static/test_1_point.json"),
            match_querystring=True,
            content_type='application/json',
        )

        result = elevation('41.889040454306752,12.525333445447737')
        self.assertIn('Point', result['geometry']['type'])
        self.assertEqual(len(result['geometry']['coordinates']), 1)
        self.assertEqual(len(result['geometry']['coordinates'][0]), 3)

    @responses.activate
    def test_2_points(self):
        responses.add(
            responses.GET,
            "https://maps.googleapis.com/maps/api/elevation/json?path=41.889040454306752%2C12.525333445447737%7C41.889050454306752%2C12.525335445447737&samples=2",
            body=self.load_fixture("tests/static/test_2_points.json"),
            match_querystring=True,
            content_type='application/json',
        )

        result = elevation('41.889040454306752,12.525333445447737|41.889050454306752,12.525335445447737')
        self.assertIn('LineString', result['geometry']['type'])
        self.assertEqual(len(result['geometry']['coordinates']), 2)
        self.assertEqual(len(result['geometry']['coordinates'][0]), 3)
        self.assertEqual(len(result['geometry']['coordinates'][1]), 3)

    @responses.activate
    def test_maximum_sampling(self):
        responses.add(
            responses.GET,
            "https://maps.googleapis.com/maps/api/elevation/json?path=41.889040454306752%2C12.525333445447737%7C41.872041927699982%2C12.582239191900001&samples=512",
            body=self.load_fixture("tests/static/test_maximum_sampling.json"),
            match_querystring=True,
            content_type='application/json',
        )

        result = elevation('41.889040454306752,12.525333445447737|41.872041927699982,12.582239191900001', sampling=4)
        self.assertIn('LineString', result['geometry']['type'])
        self.assertEqual(len(result['geometry']['coordinates']), 512)
        self.assertEqual(len(result['geometry']['coordinates'][0]), 3)
        self.assertEqual(len(result['geometry']['coordinates'][-1]), 3)

    @responses.activate
    def test_automatic_sampling(self):
        responses.add(
            responses.GET,
            "https://maps.googleapis.com/maps/api/elevation/json?path=41.8890404543067518%2C12.5253334454477372%7C41.8972185849048984%2C12.4902286938660296&samples=72",
            body=self.load_fixture("tests/static/test_automatic_sampling.json"),
            match_querystring=True,
            content_type='application/json',
        )

        result = elevation('41.8890404543067518,12.5253334454477372|41.8972185849048984,12.4902286938660296')
        self.assertIn('LineString', result['geometry']['type'])
        self.assertEqual(len(result['geometry']['coordinates']), 72)
        self.assertEqual(len(result['geometry']['coordinates'][0]), 3)
        self.assertEqual(len(result['geometry']['coordinates'][-1]), 3)

    def test_elevation_api_exception(self):
        with self.assertRaises(ElevationApiError):
            elevation('43432430,2321321320')
