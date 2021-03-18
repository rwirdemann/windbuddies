from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sessions/', views.create, name='create'),
    path('sessions/delete/<int:session_id>/', views.delete_session, name='delete'),
    path('weather/', views.actual_weather, name='actual_weather'),
]