from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def products(request):
    return HttpResponse("product")

    
def product_details(request, id):
    return HttpResponse(id)
