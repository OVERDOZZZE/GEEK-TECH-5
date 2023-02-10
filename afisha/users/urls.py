from django.urls import path
from .views import authorization, registration


urlpatterns = [
    path('authorization/', authorization),
    path('registration/', registration)
]
