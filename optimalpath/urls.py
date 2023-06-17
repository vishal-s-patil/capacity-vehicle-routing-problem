from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('optimalpath', views.optimal_path_view, name='optimal_path_view')
]
