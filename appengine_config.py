# [START vendor]
from google.appengine.ext import vendor
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'gaenv'))

# Add any libraries installed in the "lib" folder.
vendor.add('lib')
# [END vendor]
