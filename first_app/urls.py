from django.urls import path     
from .views import roots, index, new, create, show, edit, destroy, json

urlpatterns = [
    path('', roots),
    path('blogs/', index),
    path('blogs/new/', new),
    path('blogs/create/', create),
    path('blogs/<int:number>/', show),
    path('blogs/<int:number>/edit/', edit),
    path('blogs/<int:number>/delete/', destroy),
    path('blogs/json/', json),
]