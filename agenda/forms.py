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
        self.add_error(
            'first_name',
            ValidationError('Mensagem de erro', code = 'invalid ')
        )