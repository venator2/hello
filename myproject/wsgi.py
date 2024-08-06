"""
WSGI config for myproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
import sys

# Додайте шлях до вашого проекту
path = '/home/venator3/hello'
if path not in sys.path:
    sys.path.append(path)

# Встановіть змінну середовища для вашого проекту
os.environ['DJANGO_SETTINGS_MODULE'] = 'hello.settings'

# Активуйте віртуальне оточення
activate_this = '/home/venator3/hello/myenv/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), {'__file__': activate_this})

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

