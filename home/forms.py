from django import forms
from django.forms import ModelForm

from home.api import nomeAleatorio

from .models import Usuario


class UploadForm(ModelForm):
  nome = forms.CharField()
  sobrenome = forms.CharField()
  idade = forms.CharField()
  data_de_nascimento = forms.CharField()
  email = forms.EmailField()
  apelido = forms.CharField(required=False)
  observacao = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': '3'}))
  class Meta:
    model = Usuario
    fields = ['nome', 'sobrenome', 'idade', 'data_de_nascimento', 'email', 'apelido', 'observacao']

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['data_de_nascimento'].widget.attrs.update({'class': 'mask-data'})
    self.fields['idade'].widget.attrs.update({'class': 'mask-idade'})
    self.fields['nome'].initial=nomeAleatorio()