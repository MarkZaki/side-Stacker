from rest_framework import serializers
from django.contrib.auth.models import User
import django.contrib.auth.password_validation as validators
from django.core import exceptions


 

class UserSerializer(serializers.ModelSerializer):
    profile = serializers.SerializerMethodField('get_profile')
    password = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'username',
                  'password', 'password2', 'profile']
        extra_kwargs = {'password': {'write_only': True, }}

    def save(self):
        user = User(
            email=self.validated_data['email'], username=self.validated_data['username'])
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        errors = dict()
        try:
            # validate the password and catch the exception
            validators.validate_password(password=password, user=user)

            # the exception raised here is different than serializers.ValidationError
        except exceptions.ValidationError as e:
            errors['password'] = list(e.messages)
        if errors:
            raise serializers.ValidationError(errors)
        # return super(UserSerializer, self).validate_data
        if password != password2:
            raise serializers.ValidationError(
                {'password': 'Passwords Must match!'})
        user.set_password(password)
        user.save()
        return user
    # to return the user's profile when you list the users

    def get_profile(self, profile):
        profile = profiles.objects.get(user=profile)
        serializer = porfiles_Serializer(profile, many=False)
        return serializer.data
