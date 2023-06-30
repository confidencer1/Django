from django.urls import path
from . import views

urlpatterns = [
    path('members/details/<slug:slug>',views.details, name = 'details'),
    path('members/', views.members, name= 'members'),
    path('', views.main, name='main'),
    path('testing/', views.testing ,name='testing'),
]