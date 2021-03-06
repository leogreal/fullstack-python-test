from django.urls import path

from store.authentication.views import ProfileCreate, ProfileLogin

app_name = 'authentication'

urlpatterns = [
    path('signup/', ProfileCreate.as_view(), name='signup'),
    path('signin/', ProfileLogin.as_view(), name='signin'),
]
