from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.


def home(request):
    data = {
        "id": 1
    }
    return JsonResponse(data)

