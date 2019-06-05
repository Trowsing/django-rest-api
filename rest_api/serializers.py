from rest_api.models import Person, Partner
from rest_framework import serializers

class PersonSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Person
		fields = "__all__"
