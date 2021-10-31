from django.urls import path

from . import views 

urlpatterns = [
    path('echo/', views.Echo.as_view()),

    path('add-one/', views.AddOne.as_view()),
    path('get-count/', views.GetCount.as_view()),
]