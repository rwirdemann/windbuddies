from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sessions/', views.create_session, name='create_session'),
    path('sessions/delete/<int:session_id>/', views.delete_session),
    path('weather/', views.actual_weather, name='actual_weather'),
]