from django.http import JsonResponse
from rest_api.models import Person
from rest_api.serializers import PersonSerializer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def get_create_persons(request):
	if request.method == "GET":
		persons = Person.objects.all()
		serializer = PersonSerializer(persons, many=True)
		return JsonResponse({"persons":serializer.data})
		
	elif request.method == "POST":
		data = JSONParser().parse(request)
		try:
			person = Person.objects.get(pk=data["pk"])
			serializer = PersonSerializer(person, data=data)
			if serializer.is_valid():
				serializer.save()
				return JsonResponse({"updated": person.name})
			return JsonResponse({"errors": serializer.errors}, status=400)
		except Person.DoesNotExist:
			serializer = PersonSerializer(data=data)
			if serializer.is_valid():
				serializer.save()
				return JsonResponse({"person": serializer.data})
			return JsonResponse({"errors": serializer.errors}, status=400)
		
		
@csrf_exempt
def person_detail(request, pk):
	try:
		person = Person.objects.get(pk=pk)
	except Person.DoesNotExist as err:
		return JsonResponse({"error": str(err)}, status=404)
		
	if request.method == "GET":
		serializer = PersonSerializer(person)
		return JsonResponse({"person": serializer.data})
		
	if request.method == "PUT":
		data = JSONParser().parse(request)
		serializer = PersonSerializer(person, data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse({"person": serializer.data})
		return JsonResponse({"errors": serializer.errors}, status=400)
		
	if request.method == "DELETE":
		person.delete()
		return JsonResponse({"deleted": person.name}, status=204)
	
