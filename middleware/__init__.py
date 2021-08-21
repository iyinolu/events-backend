from rest_framework.request import Request
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.utils.functional import SimpleLazyObject
from django.contrib.auth.middleware import get_user
from django.utils.deprecation import MiddlewareMixin

def get_user_jwt(request):
    user = get_user(request)
    if user.is_authenticated:
        return user
    try:
        user_jwt = JWTAuthentication().authenticate(Request(request))
        if user_jwt is not None:
            return user_jwt[0]
    except: 
        pass
    return user

class AuthenticationMiddlewareJWT(MiddlewareMixin):
    """Appends User object to every authenticated request"""
    def process_request(self, request):
        assert hasattr(request, 'session')
        request.user = SimpleLazyObject(lambda: get_user_jwt(request))
    
