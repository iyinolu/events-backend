# from django.contrib.auth.models import User
# from user.serializers import UserSerializer

# def custom_jwt_response_handler(token, user=None, request=None):
#     '''
#     Manages JWT's Response Payloads
#     '''
#     user  = UserSerializer(user, context={'request': request}).data
#     user['token'] = token
#     # return user