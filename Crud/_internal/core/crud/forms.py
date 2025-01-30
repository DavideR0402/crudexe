from django import forms #type: ignore
from django.core import validators #type: ignore


class ProductValidator(forms.Form):
    """
        Product validator

    """
    producto = forms.CharField(
        max_length=100,
        validators=[
            validators.RegexValidator(
                regex=r'^[a-zA-ZáéíóúÁÉÍÓÚ\s]+$',
                code='invalid_name'
            )
        ])
