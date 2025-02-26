from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Usuario
import re

class LoginForm(AuthenticationForm):
    username = forms.EmailField(label="E-mail", required=True)
    
class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput,
        help_text="Mínimo 8 caracteres, 1 especial, 1 número e 1 maiúscula."
    )
    password2 = forms.CharField(
        label="Confirmar Senha",
        widget=forms.PasswordInput
    )

    class Meta:
        model = Usuario
        fields = ["email", "first_name", "password1", "password2"]

    def clean_first_name(self):
        nome = self.cleaned_data.get("first_name")
        if not nome.isalpha():
            raise forms.ValidationError("O nome deve conter apenas letras.")
        return nome

    def clean_password1(self):
        senha = self.cleaned_data.get("password1")
        if not re.match(r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$', senha):
            raise forms.ValidationError("A senha deve ter pelo menos 8 caracteres, incluindo 1 letra maiúscula, 1 número e 1 caractere especial.")
        return senha

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if Usuario.objects.filter(email=email).exists():
            raise forms.ValidationError("Este e-mail já está cadastrado.")
        return email
