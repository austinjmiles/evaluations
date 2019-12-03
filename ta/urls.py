from django.urls import path, include
from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('form/', views.form, name='form'),
    path('email/', views.email, name ='email'),
    path('results/', views.results, name='results')
]