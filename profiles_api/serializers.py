"""
Serializer is a feature from Django Rest Framework that allows you to
easily convert data inputs into Python objects and vice versa.

It's kind similiar to a Django form which you define and it has the various fields
that you want to accept for the input for your api.

So if we are going to add PUT or POST to APIView, we need to create a serializer to receive
the content that we POST.

"""

from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Serializers a name field for testing our APIVview"""

    name = serializers.CharField(max_length=10)
