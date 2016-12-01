from django import forms

class busca(forms.Form):
	busca = forms.CharField(max_length=100, label="Busca:", help_text="Digite a palavra que deseja buscar.", required=False)


