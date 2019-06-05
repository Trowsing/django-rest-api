from django.urls import path
from rest_api import api

urlpatterns = [
	path("persons/", api.get_create_persons),
	path("persons-detail/<int:pk>", api.person_detail),
]
