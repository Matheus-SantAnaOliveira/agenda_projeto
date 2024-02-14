from django.shortcuts import render, get_object_or_404
from agenda.models import Contact
# Create your views here.

def index(request):
    contacts = Contact.objects.filter(show=True).order_by('-id')
    context = {'contacts':contacts}
    
    return render(request, 'agenda/index.html', context= context)

# Create your views here.
def contact(request, contact_id):
    contacts = get_object_or_404(Contact.objects, pk=contact_id,show = True)
    context = {'contact':contacts}
    print(context)
    
    return render(request, 'agenda/contact.html', context= context)