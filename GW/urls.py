from django.urls import path
from . import views
from GW.dash_apps.finished_apps import Max_App , Min_App, Max_App2, Min_App2, Chart_App, Chart_App2

urlpatterns= [
    path('', views.index, name='index'),
    path('Graph1/', views.Graph1, name='Graph1'),
    path('Graph2/', views.Graph2, name='Graph2'),
]