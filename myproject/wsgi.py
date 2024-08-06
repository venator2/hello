"""
WSGI config for myproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
import sys

# Додайте шлях до вашого проекту
path = '/home/venator3/myproject'
if path not in sys.path:
    sys.path.append(path)

# Встановіть змінну середовища для вашого проекту
os.environ['DJANGO_SETTINGS_MODULE'] = 'myproject.settings'

# Активуйте віртуальне оточення
activate_this = '/home/venator3/myproject/myenv/bin/activate_this.py'
exec(open(activate_this).read(), {'__file__': activate_this})

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

