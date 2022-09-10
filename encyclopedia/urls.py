from django.urls import path

from . import views
app_name = 'encyclopedia'
urlpatterns = [
    path("", views.index, name="index"),
    path("newpage", views.newpage, name = "newpage"),
    path("random", views.random, name = "random"),
    path("wiki/<str:name>", views.article, name="article"),
    path("wiki/<str:name>/edit", views.edit, name = "edit"),
    path("search", views.search, name = "search"),
]
