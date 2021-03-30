from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sessions/', views.create, name='create'),
    path('sessions/join/<int:session_id>/',
         views.join_session,
         name='join'),
    path('sessions/unjoin/<int:session_id>/',
         views.unjoin_session,
         name='unjoin'),
    path('sessions/delete/<int:session_id>/',
         views.delete_session,
         name='delete'),
    path('weather/', views.actual_weather, name='actual_weather'),
    path('forecast/', views.forecast, name='forecast'),
    path('signup/', views.signup, name='signup'),
]