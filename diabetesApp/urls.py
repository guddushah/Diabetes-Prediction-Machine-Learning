from django.urls import path
from . import views

urlpatterns = [
    #path('',views.predictor, name='predictor'),
    path('',views.home, name='home'),
    path('predict',views.predictor, name='predict'),
    path('result',views.predictor, name='result')
    #path('home',views.home, name='home')
]