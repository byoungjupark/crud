import json

from django.http import JsonResponse
from django.views import View

from movies2.models import Actor, Movie

class ActorView(View):
    def get(self, request):
        actors = Actor.objects.all()        
        results = [
            {
                "first_name" : actor.first_name, 
                "last_name" : actor.last_name, 
                "title" : [actor_movie.movie.title for actor_movie in actor.actormovie_set.all()]
            } 
            for actor in actors
        ]

        return JsonResponse({"actors" : results}, status=200)

class MovieView(View):
    def get(self, request):
        movies = Movie.objects.all()
        results=[
            {
                "title" : movie.title,
                "release_date" : movie.release_date,
                "actor" : [movie_actor.actor.first_name for movie_actor in movie.actormovie_set.all()]
            }
            for movie in movies
        ]

        return JsonResponse({"movies":results}, status=200)
