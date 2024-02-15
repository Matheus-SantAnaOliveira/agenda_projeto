from django.urls import path
from agenda import views
app_name = 'agenda'
urlpatterns = [
    path('<int:contact_id>/', views.contact, name = 'contact'),
    path('search/', views.search, name = 'search'),
    path('',views.index, name = 'index')
]