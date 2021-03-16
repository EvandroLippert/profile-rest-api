from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


class HelloApiView(APIView):
    """Test API View"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """
        Returns a list of APIView features
        request:
            contain the details of the request being made to the API

        format:
            Used to add a format suffix to the end of the endpoint URL,
            it's a best practice to keep it.

        """

        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete',
            'Is similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs'
        ]

        # The response that it will be returned can be a list or a dictionary
        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)
        """ 
        The conditional below will verify if the requirements in the file
        serializers.py are satisfied and the post is valid.
        In this example, it will verify if the word in short than the predefined max_length.
        """
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def put(self, request, pk=None):
        """
        Handle updating an object
        It updates the entire object

        When you're doing HTTP PUT, you typically do it
        to a specific URL primery key
        """

        return Response({"method": "PUT"})

    def patch(self, request, pk=None):
        """
        Handle a partial update of an object
        It only updates the fields that were provided in the request
        so if you had a first name and a last name field, and you made a
        patch request with just providing the last name, it would only
        update the last name.
        Whereas if you did a put request and you provided the last name,
        then, in that case, it would remove the first name completely because HTTP
        put is essentially replacing an object with that was provided.
        """
        return Response({"method": "PATCH"})

    def delete(self, request, pk=None):
        """Delete an object"""

        return Response({"method": "DELETE"})
exit