from django import forms


from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate

from django import forms
from django.contrib.auth import get_user_model

class ChangePasswordForm(forms.Form):
    new_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'style': 'border-radius: 10px; width: 100%;'
        }),
        label="Nueva contraseña"
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'style': 'border-radius: 10px; width: 100%;'
        }),
        label="Confirmar nueva contraseña"
    )

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get('new_password')
        confirm_password = cleaned_data.get('confirm_password')

        if new_password != confirm_password:
            raise forms.ValidationError('Las contraseñas no coinciden')

        return cleaned_data