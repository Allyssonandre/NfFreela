import os, sys
sys.path.append('/home/nfreela/apps_wsgi/nfreela')
os.environ['PYTHON_EGG_CACHE'] = '/home/nfreela/apps_wsgi/.python-eggs'
os.environ['DJANGO_SETTINGS_MODULE'] = 'nfreela.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
