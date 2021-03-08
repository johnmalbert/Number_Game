from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('guess_lower', views.guess_lower),
    path('guess_higher', views.guess_higher),
    path('correct', views.correct),
    path('restart', views.restart),
    path('guess', views.guess),
    path('leaders', views.leaders)
]