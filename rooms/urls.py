from django.urls import path
from . import views

app_name = "roooms"

urlpatterns = [
    path("<int:pk>", views.rooms_detail, name="detail"),
    path("search/", views.search, name="search"),
]
