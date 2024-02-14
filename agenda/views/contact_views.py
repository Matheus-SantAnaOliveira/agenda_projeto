from django.shortcuts import render
from agenda.models import Contact
# Create your views here.
def index(request):
    contacts = Contact.objects.all()
    context = {'contacts':contacts}
    
    return render(request, 'agenda/index.html', context= context)