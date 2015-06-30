import responses
import unittest

from geojson_elevation.backends.google import elevation
from geojson_elevation.exceptions import ElevationApiError


class TestGoogleBackend(unittest.TestCase):

    """ Google Elevation API tests """
    @responses.activate
    def test_1_point(self):

        json = """{
           "results" : [
              {
                 "elevation" : 42.70062255859375,
                 "location" : {
                    "lat" : 41.88904045430675,
                    "lng" : 12.52533344544774
                 },
                 "resolution" : 4.771975994110107
              }
           ],
           "status" : "OK"
        }"""

        url = ""
        url += "https://maps.googleapis.com/maps/api/elevation/json"
        url += "?locations=41.889040454306752%2C12.525333445447737"
        responses.add(
            responses.GET,
            url,
            body=json,
            match_querystring=True,
            content_type='application/json',
        )

        result = elevation('41.889040454306752,12.525333445447737')
        self.assertIn('Point', result['geometry']['type'])
        self.assertEqual(len(result['geometry']['coordinates']), 1)
        self.assertEqual(len(result['geometry']['coordinates'][0]), 3)

    def test_2_points(self):
        result = elevation('41.889040454306752,12.525333445447737|41.889050454306752,12.525335445447737')
        self.assertIn('LineString', result['geometry']['type'])
        self.assertEqual(len(result['geometry']['coordinates']), 2)
        self.assertEqual(len(result['geometry']['coordinates'][0]), 3)
        self.assertEqual(len(result['geometry']['coordinates'][1]), 3)

    def test_maximum_sampling(self):
        result = elevation('41.889040454306752,12.525333445447737|41.872041927699982,12.582239191900001', sampling=4)
        self.assertIn('LineString', result['geometry']['type'])
        self.assertEqual(len(result['geometry']['coordinates']), 512)
        self.assertEqual(len(result['geometry']['coordinates'][0]), 3)
        self.assertEqual(len(result['geometry']['coordinates'][-1]), 3)

    def test_automatic_sampling(self):
        result = elevation(
            '41.8890404543067518,12.5253334454477372|41.8972185849048984,12.4902286938660296')
        self.assertIn('LineString', result['geometry']['type'])
        self.assertEqual(len(result['geometry']['coordinates']), 72)
        self.assertEqual(len(result['geometry']['coordinates'][0]), 3)
        self.assertEqual(len(result['geometry']['coordinates'][-1]), 3)

    def test_elevation_api_exception(self):
        with self.assertRaises(ElevationApiError):
            elevation('43432430,2321321320')
