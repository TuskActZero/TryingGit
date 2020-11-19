from django.urls import path, include
from logo1 import views

urlpatterns = [
    path('', views.welcome),
    path('register', views.register),
    path('login/', views.login),
    path('logout/', views.logout),
    path('add', views.add),
    path('edit/<int:persona_id>', views.edit),
    path('delete/<int:persona_id>', views.delete),
    path('', views.person),

]
