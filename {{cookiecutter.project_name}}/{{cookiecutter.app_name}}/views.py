from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.conf.urls import url, include
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json

@api_view(['GET','POST'])
def {{cookiecutter.func_name}}(request):
	if(request.method == 'POST'):
        	return Response({"message": "Your data:", "data": request.data})
	return Response({"message": "Hello world!"})
