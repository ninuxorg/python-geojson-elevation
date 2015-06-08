class ElevationException(Exception):
	""" root elevation exception """
	pass


class ElevationApiError(ElevationException):
    """
    When elevation function return error
    to convert GeoJSON
    """
    pass
