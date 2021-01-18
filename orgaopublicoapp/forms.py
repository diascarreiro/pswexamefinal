from django import forms
from .models import orgaopublico

class orgaopublicoform(forms.ModelForm):
	class Meta:
		model =orgaopublico
		fields = '__all__'
		
