from django.shortcuts import render, redirect
from django.contrib import messages
from agenda.forms import RegisterForm
def register(request):
    form = RegisterForm(request.POST)

    if form.is_valid():
        form.save()
        messages.success(request, 'Usuário registrado')
        return redirect('agenda:index')
    return render(
        request, 'agenda/register.html',
        {
            'form':form
        }
    )