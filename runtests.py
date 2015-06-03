#!/usr/bin/env python

try:
    import nose
except ImportError:
    message = """nose package not installed, install test requirements with:

    pip install -r requirements-test.txt
    """
    raise ImportError(message)

if __name__ == "__main__":
    nose.run()
