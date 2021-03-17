"""
Serializer is a feature from Django Rest Framework that allows you to
easily convert data inputs into Python objects and vice versa.

It's kind similar to a Django form which you define and it has the various fields
that you want to accept for the input for your api.

So if we are going to add PUT or POST to APIView, we need to create a serializer to receive
the content that we POST.

"""

from rest_framework import serializers

from profiles_api import models


class HelloSerializer(serializers.Serializer):
    """Serializers a name field for testing our APIVview"""

    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """
    Serializer a user profile object

    We need to define a meta class to configure the serializer
    to point to a specific model in our project.
    """

    class Meta:
        """
        At the meta class:
            * You should point the Model that you are using;
            * Specify a list of fields that you want to either make accessible
            in API or want to use to create new models with the serializer

        """
        model = models.UserProfile

        fields = ('id', 'email', 'name', 'password')

        # We added this var to avoid that the user retrieve the password,
        # because it is a flaw in security

        # We also define for the api in browser that the input field password will
        # be 'password'
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validate_data):
        """
        Create and return a new user

        It will use the UserProfileManager
        to store the password as a Hash
        """
        user = models.UserProfile.objects.create_user(
            email=validate_data['email'],
            name=validate_data['name'],
            password=validate_data['password']
        )

        return user

    def update(self, instance, validated_data):
        """
        Handle updating user account

        We need to create custom function update to store the password as a has
        if someone updates their account.

        So, we need to replace the text plain password to an encoded one
        and after that update the account
        """
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializers profile feed items"""

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {
            'user_profile': {'read_only': True}
        }
