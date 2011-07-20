import os
import sys

root_dir = '/home/cahoona/.virtualenvs/staging.eusalive.co.uk'
activate_this = root_dir + '/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

sys.path.append(root_dir + '/project')

os.environ['PYTHON_EGG_CACHE'] = '/tmp/.python-egg'
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings.staging'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
