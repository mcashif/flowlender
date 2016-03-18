from django import forms
from flowlendercms.models import ClientDetail

class ClientDetailForm(forms.ModelForm):
    class Meta:
        model = ClientDetail # Your User model
        fields = ('title', 'text',)
