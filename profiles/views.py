from rest_framework import viewsets
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import filters, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User





class user_view_set(viewsets.ModelViewSet):
    """used to create users only"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = ()

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        json = {}
        if serializer.is_valid():
            user = serializer.save()
            token = get_token(user.username)
            json['message'] = 'User created successfully!'
            json['email'] = user.email
            json['username'] = user.username
            json['token'] = token.key
        else:
            json = serializer.errors
        return Response(json, status=status.HTTP_201_CREATED)

    # def list(self, request, *args, **kwargs):
    #     json = {'message': 'you are not allowed to do that'}
    #     return Response(json, status=status.HTTP_403_FORBIDDEN)

    # def retrieve(self, request, *args, **kwargs):
    #     json = {'message': 'you are not allowed to do that'}
    #     return Response(json, status=status.HTTP_403_FORBIDDEN)

    # def update(self, request, *args, **kwargs):
    #     json = {'message': 'you are not allowed to do that'}
    #     return Response(json, status=status.HTTP_403_FORBIDDEN)

    # def partial_update(self, request, *args, **kwargs):
    #     json = {'message': 'you are not allowed to do that'}
    #     return Response(json, status=status.HTTP_403_FORBIDDEN)

    # def destroy(self, request, *args, **kwargs):
    #     json = {'message': 'you are not allowed to do that'}
    #     return Response(json, status=status.HTTP_403_FORBIDDEN)


def get_token(username):
    """post a username and a password and this will retun the token of that user"""
    new_user = User.objects.get(username=username)
    token = Token.objects.get(user=new_user)
    return token
