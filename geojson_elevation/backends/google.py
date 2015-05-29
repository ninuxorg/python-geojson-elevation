
#!/usr/bin/env python
import requests
from collections import OrderedDict

try:
    from django.contrib.gis.geos import Point, LineString
except ImportError:
    from shapely.geometry import Point, LineString


def elevation_profile(path, api_key=None, sampling=50):
    """
    Proxy to google elevation API but returns GeoJSON
    For input parameters read:
    https://developers.google.com/maps/documentation/elevation/
    """
    url = 'https://maps.googleapis.com/maps/api/elevation/json'
    params = {}

    # add api key if present
    if api_key:
        params['key'] = api_key

    points = []
    # convert path in list of Point objects
    for latlng in path.split('|'):
        latlng = latlng.split(',')
        points.append(Point(float(latlng[1]), float(latlng[0])))
    if len(points) > 1:
        # length of the path in meters
        length = LineString(points).length * 100000
        # get 1 point every x meters, where x is defined in ELEVATION_DEFAULT_SAMPLING
        samples = int(round(length / sampling))
        # use the automatically calculated value as long as it is compatibile with the API usage limits
        params['samples'] = samples if samples <= 512 else 512
    # send request to Google Elevation API
    response = requests.get(url, params=params)
    data = response.json()

    # if ok convert to GeoJSON
    if data['status'] == 'OK':
        # if more than one result use LineString
        if len(data['results']) > 1:
            geometry = 'LineString'
        # else use Point
        else:
            geometry = 'Point'
        # lng, lat, z coordinates
        coordinates = []
        for point in data['results']:
            coordinates.append([point['location']['lng'],
                                point['location']['lat'],
                                point['elevation']])
        return OrderedDict((
            ('type', 'Feature'),
            ('geometry', OrderedDict((
                ('type', geometry),
                ('coordinates', coordinates)
            )))
        ))
    # else return original response
    else:
        return data
