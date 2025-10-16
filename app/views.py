from django.shortcuts import render
def index(request):
    context = {"name" : "Manon", "breadcrumb" : [('Home', '/')]}
    return render(request, "index.html", context)
