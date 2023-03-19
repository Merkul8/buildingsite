from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control py-3', 'placeholder': "Ваше имя*"}))
    phone_number = forms.IntegerField(label='', widget=forms.TextInput(attrs={'class': 'form-control py-3', 'placeholder': "Ваш номер*"}))
    email = forms.EmailField(label='', required=False,widget=forms.EmailInput(attrs={'class': 'form-control py-3', 'placeholder': "Ваш e-mail"}))
    comment = forms.CharField(label='', required=False,widget=forms.TextInput(attrs={'class': 'form-control py-3', 'rows': 5, 'placeholder': "Комментарий"}))
    