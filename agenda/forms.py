from agenda.models import Contact
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
class ContactForm(forms.ModelForm):
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept':'image/*',
            }
        )
    )
    first_name = forms.CharField(
        widget= forms.TextInput(
            attrs={
                'class':'classe-a',
                'placeholder':'DIgite seu nome'
                }
            ), help_text='Insira seu primeiro nome'
        )
    
    last_name = forms.CharField(
        widget= forms.TextInput(
            attrs={ 'class':'class-b',
                    'placeholder':'Digite seu sobrenome'
            }
        ), help_text='Insira seu sobrenome'
    )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    class Meta:
        model = Contact
        fields = ('first_name','last_name', 'phone',
                  'email', 'description','category','picture',)
       
    def clean(self):
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name == last_name:
            msg = ValidationError(
                'Primeiro nome não pode ser igual ao segundo',
                code='invalid'
            )
            self.add_error('first_name', msg)
            self.add_error('last_name', msg)

        return super().clean()

    def clean_first_name(self):
        data = self.cleaned_data.get("first_name")
        if data == 'ABC':
            self.add_error('first_name' ,
                        ValidationError('Não digite ABC neste campo', 
                                        code='invalid'))
        return data
    
    def clean_last_name(self):
        cleaned_data = self.cleaned_data.get("last_name")
            
        if cleaned_data == 'DEF':
            self.add_error('last_name',
                            ValidationError('Não digite DEF neste campo', 
                                            code='invalid'))
        return cleaned_data

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        required=True,
        min_length=3,
    )
    last_name = forms.CharField(
        required=True,
        min_length=3,
    )
    email = forms.CharField(
        required=True,
        min_length=3,
    )
    class Meta:
        model = User
        fields =(
            'first_name', 'last_name', 'email',
            'username', 'password1', 'password2',
        )
    def clean_email(self):
        email = self.cleaned_data.get('email')
        
        if User.objects.filter(email=email).exists():
            self.add_error(
                'email', ValidationError('Ja existe este e-mail', code = 'invalid')
            )
        return email