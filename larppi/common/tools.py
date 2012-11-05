__author__ = 'incidence'

from django.conf import settings
import datetime

def set_cookie(response, key, value, expire=None):
    if expire is None:
        max_age = 365*24*60*60  # One year
    else:
        max_age = expire
    expires = datetime.datetime.strftime(datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age), "%a, %d-%b-%Y %H:%M:%S GMT")
    response.set_cookie(key, value, max_age=max_age, expires=expires,
        domain=settings.SESSION_COOKIE_DOMAIN, secure=settings.SESSION_COOKIE_SECURE or None)