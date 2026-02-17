from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('player/<str:username>/', views.PlayerDetailView.as_view(), name='player'),
]