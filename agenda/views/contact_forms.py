from typing import Any
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.db.models import Q
from agenda.models import Contact
from django.core.paginator import Paginator
from django import forms
from django.core.exceptions import ValidationError
from django.contrib import messages

# Create your views here.
from agenda.forms import ContactForm

def create(request):
    form_action = reverse("agenda:create")
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        context = {
            'form': form,
            'form_action':form_action
        }
        if form.is_valid():
            contact = form.save()
            messages.success('Usúario criado com sucesso')
            return redirect('agenda:update', contact_id=contact.pk )
        
        return render(request, 'agenda/create.html', context= context)
    
    form = ContactForm() 
    context = {
            'form': form,
            'form_action':form_action
        } 
    return render(request, 'agenda/create.html', context= context)

def update(request, contact_id):
    contact = get_object_or_404(
        Contact, pk = contact_id, show = True
        )
    form_action = reverse("agenda:update", args=(contact_id,))
    
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES, instance = contact)
        
        context = {
            'form': form,
            'form_action':form_action
        }
        if form.is_valid():
            contact = form.save()
            messages.success('Usúario editado com sucesso')
            return redirect('agenda:update', contact_id = contact.pk )
        
        messages.warning('algo deu errado')
        return render(request, 'agenda/create.html', context= context)
    
    form = ContactForm(instance = contact) 
    context = {
            'form': form,
            'form_action':form_action
        }
    return render(request, 'agenda/create.html', context= context)
    

def delete(request, contact_id):
    contact = get_object_or_404(
        Contact, pk = contact_id, show = True
        )
    confirmation = request.POST.get('confirmation', 'no')
    if confirmation =='yes':
        contact.delete()
        messages.warning('Usúario deletado')
        return redirect("agenda:index")
    
    return render(request, 
                  'agenda/contact.html',
                  {'contact':contact,
                   'confirmation' : confirmation})