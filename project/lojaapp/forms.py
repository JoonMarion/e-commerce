from django import forms
from django.db.models import fields
from .models import *
from django.forms import ModelForm, TextInput, EmailInput


class Checar_PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido_order
        fields = ['ordenado_por', 'endereco_envio', 'telefone', 'email']

        widgets = {
            'ordenado_por': TextInput(attrs={
                'class': 'form-control',
                'style': 'max-width: 300px;',
                'placeholder': 'Nome Completo'
            }),

            'endereco_envio': TextInput(attrs={
                'class': 'form-control',
                'style': 'max-width: 300px;',
                'placeholder': 'Endereço'
            }),

            'telefone': TextInput(attrs={
                'class': 'form-control',
                'style': 'max-width: 300px;',
                'placeholder': 'Telefone'
            }),

            'email': EmailInput(attrs={
                'class': 'form-control',
                'style': 'max-width: 300px;',
                'placeholder': 'Email'
            }),
        }


class ClienteRegistrarForm(forms.ModelForm):
    usuario = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'style': 'max-width: 300px;',
            'placeholder': 'Usuário'
        }
    ))

    senha = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'style': 'max-width: 300px;',
            'placeholder': 'Senha'
        }
    ))

    email = forms.CharField(widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'style': 'max-width: 300px;',
            'placeholder': 'Email'
        }
    ))

    class Meta:
        model = Cliente
        fields = ['usuario', 'senha', 'email', 'nome', 'endereco']

        widgets = {
            'endereco': TextInput(attrs={
                'class': 'form-control',
                'style': 'max-width: 300px;',
                'placeholder': 'Endereço'
            }),

            'nome': TextInput(attrs={
                'class': 'form-control',
                'style': 'max-width: 300px;',
                'placeholder': 'Nome Completo'
            })
        }
