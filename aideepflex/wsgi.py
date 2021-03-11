"""
WSGI config for aideepflex project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv


# project_folder = os.path.expanduser('./aideepflex')  # adjust as appropriate
# load_dotenv(os.path.join(project_folder, 'env.sh'))

settings_module = "aideepflex.production" if 'WEBSITE_HOSTNAME' in os.environ else 'aideepflex.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

application = get_wsgi_application()
