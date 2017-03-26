#!/WebHA/catworld/featureanalytics-443S/all_virtual_envs/data_upload_tool/bin/python

#activate_this = '/WebHA/catworld/featureanalytics-443S/webpython/bin/activate_this.py'
#exec(open(activate_this).read())

import sys
import logging

logging.basicConfig(stream=sys.stderr)
#sys.path.insert(0,"/WebHA/catworld/featureanalytics-443S/dataupload_app/")

from app import theapp as application
application.secret_key = 'mysecretkey'
