from django.urls import path, include
from rest_framework import routers
from .views import *


router = routers.DefaultRouter()
router.register(r'directors', DirectorViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'movies', MovieViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/<slug:slug>/', main_view),
    path('api/v1/<slug:slug>/<int:id>/', main_detail_view),
    path('api/v1/movies/reviews/', movies_and_reviews),
]
