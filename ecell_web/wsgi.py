# This file contains the WSGI configuration required to serve up your
# web application at http://krishanonymous.pythonanywhere.com/
# It works by setting the variable 'application' to a WSGI handler of some
# description.
#
# The below has been auto-generated for your Django project

import os
import sys


# set environment variable to tell django where your settings.py is
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecell.settings')


# serve django via WSGI
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
app=application

