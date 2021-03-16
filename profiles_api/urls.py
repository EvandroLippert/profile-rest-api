"""
Router --> Class provided by the Django Rest Framework in order
to generate the different routes that are available for our ViewSet.

So with our ViewSet you may be accessing the list request which is
just the route of our API and in this case, you would use a different
URL.

"""

from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profiles_api import views

"""
First we need to define a Default Router:
"""
router = DefaultRouter()

"""
To register the specific ViewSet with out router we use the function
register()

The first argument is the name of the URL that we wish to create;
The second argument is the ViewSet that we create at views.py
The third argument is the base name. This is going to be used for retrieving
the URLs in our router.
"""
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet)
"""
Finally, we need to add the path at the urlpatterns
"""
urlpatterns = [
    path('hello-view', views.HelloApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls))
]
