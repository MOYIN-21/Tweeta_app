from django.urls import  path
from . import views

urlpatterns =[
    path('home/', views.welcome),
    path('hello/<str:name>/', views.hello),
    path('<int:num>/', views.number)
]