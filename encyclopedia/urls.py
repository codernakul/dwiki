from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search, name="search"),
    path("wiki/<str:name>", views.article, name="article"),
    path("wiki/<str:name>/edit", views.edit, name="edit"),
    path("new", views.new, name="new"),
    path("randp", views.randp, name="randp")
]
