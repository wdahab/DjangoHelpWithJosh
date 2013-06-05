import os
import sys, socket

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
SITE_ROOT = os.path.dirname(os.path.realpath(__file__))

if SITE_ROOT not in sys.path:
	sys.path.append(SITE_ROOT)

import django.core.handlers.wsgi
_application = django.core.handlers.wsgi.WSGIHandler()

def application(environ, start_response):
    return _application(environ, start_response) 

if not socket.gethostname().startswith('Penguin'):
	import monitor
	monitor.start(interval=1.0)
