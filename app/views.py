from django.shortcuts import render
from app import settings
import os
from django.http import FileResponse

def index(request):
    path = settings.BASE_DIR / 'data'
    context = {"files" : os.listdir(path), "breadcrumb" : [('Home', '/')]}
    return render(request, "index.html", context)

def details(request, path):
    context = {"path" : path, "breadcrumb" : [('Home', '/'), (path, request.path)]}
    return render(request, "details.html", context)

def visu(request, path):
    return FileResponse(open(settings.BASE_DIR / 'data' / path, 'rb'))