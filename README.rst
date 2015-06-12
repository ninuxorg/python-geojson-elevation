python-geojson-elevation
========================

.. image:: https://travis-ci.org/ninuxorg/python-geojson-elevation.png
   :target: https://travis-ci.org/ninuxorg/python-geojson-elevation

.. image:: https://coveralls.io/repos/ninuxorg/python-geojson-elevation/badge.png
  :target: https://coveralls.io/r/ninuxorg/python-geojson-elevation

.. image:: https://landscape.io/github/ninuxorg/python-geojson-elevation/master/landscape.png
   :target: https://landscape.io/github/ninuxorg/python-geojson-elevation/master
   :alt: Code Health

.. image:: https://requires.io/github/ninuxorg/python-geojson-elevation/requirements.png?branch=master
   :target: https://requires.io/github/ninuxorg/python-geojson-elevation/requirements/?branch=master
   :alt: Requirements Status

.. image:: https://badge.fury.io/py/geojson-elevation.png
   :target: https://pypi.python.org/pypi/geojson-elevation

.. image:: https://img.shields.io/pypi/dm/geojson-elevation.svg
   :target: https://pypi.python.org/pypi/geojson-elevation

------------

GeoJSON proxy to popular elevation web services.

Currently only Google Elevation API is implemented.

**New backends or improvements very welcome!**

Tribute to `Nodeshot <https://github.com/ninuxorg/nodeshot>`__ and `Leaflet.Elevation <https://github.com/MrMufflon/Leaflet.Elevation>`__
-----------------------------------------------------------------------------------------------------------------------------------------

This code was originally written for `Nodeshot <https://github.com/ninuxorg/nodeshot>`__
in order to add an elevation profile feature using the wonderful
`Leaflet.Elevation <https://github.com/MrMufflon/Leaflet.Elevation>`__ javascript plugin.

Later the code was refactored and extracted into this python package.

Install stable version from pypi
--------------------------------

Install via pip::

    pip install geojson_elevation

Install development version
---------------------------

Install tarball:

.. code-block:: shell

    pip install https://github.com/ninuxorg/python-geojson-elevation/tarball/master

Alternatively you can install via pip using git:

.. code-block:: shell

    pip install -e git+git://github.com/ninuxorg/python-geojson-elevation#egg=geojson-elevation

If you want to contribute, install your cloned fork:

.. code-block:: shell

    git clone git@github.com:<your_fork>/python-geojson-elevation.git
    cd python-geojson-elevation
    python setup.py develop

Basic Usage Example
-------------------

.. code-block:: python

    from geojson_elevation.google import elevation

    # 1 point
    elevation('41.889040454306752,12.525333445447737')

    # path
    elevation('41.889040454306752,12.525333445447737|41.889050454306752,12.525335445447737')

Running tests
-------------

Install your forked repo:

.. code-block:: shell

    git clone git://github.com/<your_fork>/python-geojson-elevation
    cd python-geojson-elevation/
    python setup.py develop

Install test requirements:

.. code-block:: shell

    pip install -r requirements-test.txt

Run tests with:

.. code-block:: shell

    ./runtests.py

Alternatively, you can use the ``nose`` command (which has a ton of available options):

.. code-block:: shell

    nosetests
    nosetests tests.google_tests  # run only google elevation API tests

See test coverage with:

.. code-block:: shell

    coverage run --source=geojson_elevation runtests.py && coverage report

Contribute
----------

1. Join the `mailing list`_
2. Fork this repo and install it
3. Follow `PEP8, Style Guide for Python Code`_
4. Write code
5. Write tests for your code
6. Ensure all tests pass
7. Ensure test coverage is not under 90%
8. Document your changes
9. Send pull request

.. _PEP8, Style Guide for Python Code: http://www.python.org/dev/peps/pep-0008/
.. _mailing list: http://ml.ninux.org/mailman/listinfo/ninux-dev
