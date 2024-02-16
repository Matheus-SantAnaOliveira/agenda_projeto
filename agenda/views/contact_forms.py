from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from agenda.models import Contact
from django.core.paginator import Paginator
# Create your views here.

def create(request):
    query = request.POST.get('first_name')
    context = {}
    return render(request, 'agenda/create.html', context= context)
