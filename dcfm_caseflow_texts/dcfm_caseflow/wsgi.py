# Original path: dcfm_caseflow/wsgi.py


import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dcfm_caseflow.settings')
application = get_wsgi_application()
