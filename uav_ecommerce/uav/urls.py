from django.urls import path
from . import views
# http://127.0.0.1:8000/            => homepage
# http://127.0.0.1:8000/index       => homepage
# http://127.0.0.1:8000/uavs       => uavs
# http://127.0.0.1:8000/uavs/3     => uav-details

urlpatterns = [
    path("", views.index, name="home"),
    path("index", views.index),
    path("uavs", views.uavs, name="uavs"),
    path("category/<slug:slug>", views.uavs_by_category, name="uavs_by_category"),
    path("uavs/<slug:slug>", views.uav_details, name="uav_details"),
]