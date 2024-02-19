from django.shortcuts import render, redirect
from django.contrib import messages, auth
from agenda.forms import RegisterForm, RegisterUpdateForm
from django.contrib.auth.forms import AuthenticationForm
def register(request):
    form = RegisterForm(request.POST)

    if form.is_valid():
        form.save()
        messages.success(request, 'Usuário registrado')
        return redirect('agenda:login')
    
    return render(
        request, 'agenda/register.html',
        {
            'form':form
        }
    )
    

def login_view(request):
    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, 'Logado com sucesso!')
            return redirect('agenda:index')
        messages.error(request, 'Login inválido')

    return render(
        request,
        'agenda/login.html',
        {
            'form': form
        }
    )

def logout_view(request):
    auth.logout(request)
    messages.success(request, "Usúario saiu")
    return redirect('agenda:login')


def user_update(request):
    form = RegisterUpdateForm(instance=request.user)
    if request.method != 'POST':
        return render(
            request,
            'agenda/register.html',
            {
                'form': form
            }
        )
    
    form = RegisterUpdateForm(data = request.POST, instance=request.user)
    if not form.is_valid():
        return render(
            request,
            'agenda/register.html',
            {
                'form': form
            }
        )
    form.save()
    messages.success(request, 'Usúario atualizado com sucesso')
    return redirect('agenda:index')