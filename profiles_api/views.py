from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

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
