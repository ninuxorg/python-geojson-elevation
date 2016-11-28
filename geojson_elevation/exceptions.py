class GeojsonElevationException(Exception):

    """ root geojson_elevation exception """
    pass


class ElevationApiError(GeojsonElevationException):

    """
    Raised if the elevation web service response is not ok
    """
    pass
