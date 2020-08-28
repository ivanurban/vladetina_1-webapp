from django import forms


from .models import Obavestenje


class ObavestenjeModelForm(forms.ModelForm):
	class Meta:
		model = Obavestenje 
		fields = ['naslov', 'sadrzaj', 'dokument']