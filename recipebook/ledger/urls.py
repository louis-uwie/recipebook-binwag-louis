# <appname>/urls.py
from django.urls import path
from . import views

urlpatterns = [

    path('recipes/list/', views.recipe_list, name="recipe_list"),
    path('recipes/<int:id>/', views.recipe_detail, name="recipe_detail"),

    ]