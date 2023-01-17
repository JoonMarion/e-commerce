from django import forms
from django.db.models import fields
from .models import *
from django.forms import ModelForm, TextInput, EmailInput
from django.contrib.auth.models import User


class Checar_PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido_order
        fields = ['ordenado_por', 'endereco_envio', 'telefone', 'email']

        # widgets = {
        #     'ordenado_por': TextInput(attrs={
        #         'class': 'form-control',
        #         'style': 'max-width: 300px;',
        #         'placeholder': 'Nome Completo'
        #     }),
        #
        #     'endereco_envio': TextInput(attrs={
        #         'class': 'form-control',
        #         'style': 'max-width: 300px;',
        #         'placeholder': 'Endereço'
        #     }),
        #
        #     'telefone': TextInput(attrs={
        #         'class': 'form-control',
        #         'style': 'max-width: 300px;',
        #         'placeholder': 'Telefone'
        #     }),
        #
        #     'email': EmailInput(attrs={
        #         'class': 'form-control',
        #         'style': 'max-width: 300px;',
        #         'placeholder': 'Email'
        #     }),
        # }


class ClienteRegistrarForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.CharField(widget=forms.EmailInput())

    class Meta:
        model = Cliente
        fields = ['username', 'password', 'email', 'nome', 'endereco']

    def clean_username(self):
        unome = self.cleaned_data.get("username")
        if User.objects.filter(username=unome).exists():
            raise forms.ValidationError("Este usuário já existe")
        return unome


class ClienteEntrarForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
