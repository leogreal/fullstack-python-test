from django.urls import path

from store.authentication.views import ProfileCreate

app_name = 'authentication'

urlpatterns = [
    path('signup/', ProfileCreate.as_view(), name='signup'),
]
