from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    GenreListCreateView, GenreDetailView,
    ActorListCreateView, ActorDetailView,
    CinemaHallViewSet, MovieViewSet
)

app_name = "cinema"
router = DefaultRouter()
router.register("cinema_halls", CinemaHallViewSet, basename="cinema_halls")
router.register("movies", MovieViewSet, basename="movies")

urlpatterns = [
    path("genres/", GenreListCreateView.as_view()),
    path("genres/<int:pk>/", GenreDetailView.as_view()),
    path("actors/", ActorListCreateView.as_view()),
    path("actors/<int:pk>/", ActorDetailView.as_view()),
    path("", include(router.urls)),
]
