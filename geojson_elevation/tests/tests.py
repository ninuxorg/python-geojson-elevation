#!/usr/bin/env python
import sys
import os.path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from backends.google import elevation_profile

path = "41.889040454306752,12.525333445447737|41.872041927699982,12.582239191900001"
result = elevation_profile(path, None, 50)
print result