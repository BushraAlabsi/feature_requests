import sys
import logging
 
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/html/feature_requests/")
 
from run import app as application
