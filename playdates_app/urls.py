from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('dashboard', views.dashboard), #/dashboard
    path('logout', views.logout),
    path('new', views.new), #/new
    path('create', views.add_an_event), #/create
    path('<int:event_id>/edit', views.edit),#/1/edit
    path('<int:event_id>/update', views.update),
    path('<int:event_id>', views.event),#/1
    path('<int:event_id>/delete', views.delete),# 1/delete
    path('<int:event_id>/add', views.add_to),
    path('<int:event_id>/remove', views.remove_from),
]