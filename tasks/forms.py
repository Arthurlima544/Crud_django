from django import forms
from django.forms import ModelForm
from .models import * # importa todo o arquivo


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'#vai pegar todos os fields do models que eu quero para meu formulario
        #exclude = fields que eu quero ignorar..