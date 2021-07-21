import json

from django.http import JsonResponse
from django.views import View

from movies.models import Actor, Movie
# 배우 테이블과 영화 테이블은 둘의 id로 연결되어 있는데,
# 중간 테이블에서 배우id와 영화id를 참조하고 있음
# 

class ActorView(View):
    def get(self, request):
        actors = Actor.objects.all()
        results = []

        for actor in actors:
            movies = actor.movie_set.all()
            results.append(
                {
                    "first_name" : actor.first_name,
                    "last_name" : actor.last_name,
                    "title" : [movie.title for movie in movies]
                }
            )
        return JsonResponse({"result":results}, status=200)

class MovieView(View):
    def get(self,request):
        movies = Movie.objects.all()
        results = []

        for movie in movies:
            actors = movie.actor.all()
            results.append(
                {
                    "title" : movie.title,
                    "release_date" : movie.release_date,
                    "run_time" : movie.run_time,
                    "actor" : [actor.first_name for actor in actors]
                }
            )
        return JsonResponse({"result":results}, status=200)
