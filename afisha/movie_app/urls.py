from django.urls import path
from .views import *


urlpatterns = [
    path('api/v1/<slug:slug>/', main_view),
    path('api/v1/<slug:slug>/<int:id>/', main_detail_view),
    # path('api/v1/directors', directors_view),
    # path('api/v1/movies/<int:id>/', movies_view),
    # path('api/v1/reviews', reviews_view),
]
