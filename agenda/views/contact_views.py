from django.shortcuts import render

# Create your views here.
context = {}
def index(request):
    return render(request, 'agenda/index.html', context= context)