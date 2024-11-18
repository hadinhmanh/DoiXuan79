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

def gioithieu(request):
    return render(request, 'pages/about.html',{})

def sukien(request):
    return render(request, 'pages/even.html',{})

def booking(request):
    return render(request, 'pages/booking.html',{})

def dichvu(request):
    return render(request, 'pages/service.html',{})

def blog(request):
    return render(request, 'pages/blog.html',{})

def lienhe(request):
    return render(request, 'pages/contact.html',{})

# View ra các trang dịch vụ
def lauNuong(request):
    return render(request, 'pages/lauNuong.html',{})
def cheothuyen(request):
    return render(request, 'pages/cheothuyen.html',{})
def cafe(request):
    return render(request, 'pages/cafe.html',{})
def camping(request):
    return render(request, 'pages/camping.html',{})
def vuichoi(request):
    return render(request, 'pages/khuvuichoi.html',{})