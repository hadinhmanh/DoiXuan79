from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.shortcuts import render

from django.http import HttpResponse
from django.core.paginator import Paginator
from django.http import JsonResponse
import json

def index(request):
    return render(request, 'pages/index.html', {})