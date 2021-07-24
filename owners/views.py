import json

from django.http import JsonResponse
from django.views import View

from owners.models import Owner, Dog

class OwnerView(View):
    def post(self, request):
        data = json.loads(request.body)
        owner = Owner.objects.create(
            name = data["name"],
            email = data["email"],
            age = data["age"]
        )
        return JsonResponse({"MESSAGE":"CREATED"}, status=201)

    def get(self, request):
        owners = Owner.objects.all()
        results = []

        for owner in owners:
            results.append(
                {
                    "name" : owner.name,
                    "age" : owner.age,
                    "email" : owner.email,
                    "dog" : list(Dog.objects.filter(owner_id=owner.id).values('name', 'age'))
                }  
            )
        return JsonResponse({"result":results}, status=200)

# 클라이언트에서 강아지 정보 입력할때 주인정보는 이미 Post 및 데이터베이스 저장되어야 함
# 이 강아지가 이 주인인지 매칭시키려면, 우선 데이터베이스에 있는 주인 정보 가져오고 
# 클라이언트가 입력한 주인 id와 같은 것이 강아지 주인으로 등록

class DogView(View):
    def post(self, request):
        data = json.loads(request.body) # 클라이언트에서 넘어온 정보는 강아지 정보 + 주인 id 정도라고 하고
        dog = Dog.objects.create(
            # 강아지 주인 찾아주기 : 데이터베이스 주인 id == 클라이언트 주인 id이면 강아지 주인임
            # 클라이언트가 입력할 주인id의 key name은 내가 정함
            owner = Owner.objects.get(id=data["owner_id"]), 
            name = data["name"],
            age = data["age"]
        )
        return JsonResponse({"MESSAGE":"CREATED"}, status=201)
    
    def get(self, request):
        dogs = Dog.objects.all()
        results = []

        for dog in dogs:
            results.append(
                {
                    "name" : dog.name,
                    "age" : dog.age,
                    "owner" : dog.owner.name
                }
            )
        return JsonResponse({"result":results}, status=200)
