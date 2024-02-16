from django.urls import path
from agenda import views
app_name = 'agenda'
urlpatterns = [
    path('',views.index, name = 'index'),
    path('search/', views.search, name = 'search'),
    #CRUD
    path('contact/<int:contact_id>/detail/', views.contact, name = 'contact'),
    path('contact/create/', views.create, name = 'create'),
]