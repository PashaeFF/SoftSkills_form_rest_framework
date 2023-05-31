from django.conf import settings
from rest_framework import exceptions
import jwt


def authorization(request):
    try:
        payload = jwt.decode(request.auth, settings.SECRET_KEY, algorithms=['HS256'])
        return payload
    except:
        raise exceptions.AuthenticationFailed("Unauthenticated...")