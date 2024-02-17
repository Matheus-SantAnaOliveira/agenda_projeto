from agenda.models import Contact
from django.core.exceptions import ValidationError
from django import forms
class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget= forms.TextInput(
            attrs={
                'class':'classe-a',
                'placeholder':'DIgite seu nome'
                }
            ), help_text='texto de ajuda'
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
        fields = ('first_name','last_name', 'phone',)
        # widgets = {
        #     'first_name':forms.TextInput(
        #         attrs={'class':'classe-a',
        #                'placeholder':'Digite seu nome'}),}    
       
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
        aaa = self.cleaned_data.get("last_name")
        for i in self.cleaned_data:
            print(i)
            
        if aaa == 'DEF':
            self.add_error('last_name',
                            ValidationError('Não digite DEF neste campo', 
                                            code='invalid'))
        return aaa