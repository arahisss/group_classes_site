"""
WSGI config for group_classes_site project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os, sys

sys.path.insert(0, '/home/std/group_classes_site')
sys.path.insert(1, '/home/std/environments/my_env/lib/python3.10/site-packages')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'group_classes_site.settings')

application = get_wsgi_application()
