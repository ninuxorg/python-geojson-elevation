try:
    from django.contrib.gis.geos import Point, LineString
except ImportError:
    try:
        from shapely.geometry import Point, LineString
    except ImportError:
        raise ImportError("""geos wrapper missing, install either django or shapely:

        pip install django

        if you don't use the django framework, shapely is probably a better choice:

        pip install shapely
        """)
