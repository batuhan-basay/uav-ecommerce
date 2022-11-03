from django.http.response import HttpResponse
from django.shortcuts import render
from uav.models import Uav, Category
from django.utils.safestring import mark_safe


def index(request):
    context = {
        "uavs": Uav.objects.filter(is_active=True, is_home=True),
        "categories": Category.objects.all()
        
    }
    
    return render(request, "uav/index.html", context)

def uavs(request):
    context = {
        "uavs": Uav.objects.filter(is_active=True),
        "categories": Category.objects.all()
    }
    return render(request, "uav/uavs.html", context)

def uav_details(request, slug):
    uav = Uav.objects.get(slug=slug)
    return render(request, "uav/uav-details.html", {
        "uav": uav
    })

def uavs_by_category(request, slug):
    context = {
        "uavs": Category.objects.get(slug=slug).uav_set.filter(is_active=True),
        "categories": Category.objects.all(),
        "selected_category": slug
    }
    return render(request, "uav/uavs.html", context)
