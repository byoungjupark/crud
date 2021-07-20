from django.urls import path

from owners.views import OwnerView, DogView

def get(request):
    return "pong"

urlpatterns = [
    path("owner/", OwnerView.as_view()),
    path("dog/", DogView.as_view()),
]
