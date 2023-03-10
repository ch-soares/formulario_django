from django import forms


class CadastroForm(forms.Form):
    nome = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True)
    idade = forms.IntegerField(required=True)
