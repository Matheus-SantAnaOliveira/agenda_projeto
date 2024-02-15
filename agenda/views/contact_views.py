from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from agenda.models import Contact
# Create your views here.

def index(request):
    contacts = Contact.objects.filter(show=True).order_by('-id')
    context = {'contacts':contacts,
               'site_title':'contatos- '}
    
    return render(request, 'agenda/index.html', context= context)


def search(request):
    search = request.GET.get('q','').strip()
    if search == '':
        return redirect('agenda:index')
    contacts = Contact.objects\
                .filter(show=True)\
                .filter(Q(first_name__icontains=search) |
                        Q(last_name__icontains=search) |
                        Q(phone__icontains=search) |
                        Q(email__icontains=search))\
                .order_by('-id')
    context = {'contacts':contacts,
               'site_title':'search- ',
               'search_value' : search}
    
    return render(request, 'agenda/index.html', context= context)
# Create your views here.
def contact(request, contact_id):
    contacts = get_object_or_404(Contact.objects, pk=contact_id,show = True)
    site_title = f'{contacts.first_name} {contacts.last_name} '
    context = {'contact':contacts,
               'site_title':site_title}
    print(context)
     
    return render(request, 'agenda/contact.html', context= context)
