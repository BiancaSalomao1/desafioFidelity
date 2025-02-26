from django import forms
from django.core.exceptions import ValidationError
import re

class LoginForm(forms.Form):
    email = forms.EmailField(label='E-mail')
    senha = forms.CharField(label='Senha', widget=forms.PasswordInput)

class RegistrarForm(forms.Form):
    nome = forms.CharField(label='Nome')
    email = forms.EmailField(label='E-mail')
    senha = forms.CharField(label='Senha', widget=forms.PasswordInput)
    confirmar_senha = forms.CharField(label='Confirmar Senha', widget=forms.PasswordInput)

    def clean_nome(self):
        nome = self.cleaned_data['nome']
        if not re.match(r'^[a-zA-Z\s]+$', nome):
            raise ValidationError('Nome deve conter apenas letras e espaços.')
        return nome

    def clean_senha(self):
        senha = self.cleaned_data['senha']
        if len(senha) < 8 or not re.search(r'[A-Z]', senha) or not re.search(r'[a-z]', senha) or not re.search(r'[0-9]', senha) or not re.search(r'[!@#$%^&*(),.?":{}|<>]', senha):
            raise ValidationError('Senha deve ter pelo menos 8 caracteres, 1 letra maiúscula, 1 letra minúscula, 1 número e 1 caractere especial.')
        return senha

    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get('senha')
        confirmar_senha = cleaned_data.get('confirmar_senha')

        if senha and confirmar_senha and senha != confirmar_senha:
            self.add_error('confirmar_senha', 'As senhas não coincidem.')

        return cleaned_data