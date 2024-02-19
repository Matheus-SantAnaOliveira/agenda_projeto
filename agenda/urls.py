from django.urls import path
from agenda import views

app_name = 'agenda'
urlpatterns = [
    path('',views.index, name = 'index'),
    path('search/', views.search, name = 'search'),
    #CRUD
    path('contact/<int:contact_id>/detail/', views.contact, name = 'contact'),
    path('contact/create/', views.create, name = 'create'),
    path('contact/<int:contact_id>/update/', views.update, name = 'update'),
    path('contact/<int:contact_id>/delete/', views.delete, name = 'delete'),
   
   #USER
    path('user/create/', views.register, name = 'register'),
    
]   