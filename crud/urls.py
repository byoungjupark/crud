from django.urls import path, include

urlpatterns = [
    path("owners/", include("owners.urls")),
    path("movies/", include("movies.urls")),
    path("movies2/", include("movies2.urls"))
]
