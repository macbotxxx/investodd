from django import forms

class DepositForm(forms.Form):
    amount = forms.IntegerField(
        widget=forms.TextInput(attrs={
        'class': 'form-control form-control-lg form-control-number',
        'placeholder': '$ USD',
        'type': 'number',
    })
    )