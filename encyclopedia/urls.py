from django.urls import path

from . import views
app_name = 'encyclopedia'
urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.article, name="article")
]
