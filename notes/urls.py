

from django.urls import path
from . import views

app_name = 'notes'
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    # path('list_view/', views.list_note, name='list_note'),
    path('list/', views.list_notes, name='list_notes'),
    path('edit/<int:id>/', views.edit_note, name='edit_note'),
    path('delete/<int:id>/', views.delete_note, name='delete_note'),
]