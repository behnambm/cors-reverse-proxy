from django.urls import path

from . import views 

urlpatterns = [
    path('echo/', views.Echo.as_view()),
    path('echo2/', views.Echo2.as_view()),
]