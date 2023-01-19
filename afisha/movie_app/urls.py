from django.urls import path
from .views import *


urlpatterns = [
    path('api/v1/<slug:slug>/', main_view),
    path('api/v1/<slug:slug>/<int:id>/', main_detail_view),
    path('api/v1/movies/reviews', movies_and_reviews)
]
