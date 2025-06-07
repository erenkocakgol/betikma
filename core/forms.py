# betikma/forms.py
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label='Adınız Soyadınız',
        widget=forms.TextInput(attrs={
            'placeholder': 'Adınız Soyadınız',
            # **Değişiklik:** Arka plan rengi eklendi (bg-gray-50) ve border rengi ayarlandı.
            'class': 'w-full px-4 py-2 bg-gray-50 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-dark-green focus:border-dark-green'
            # Not: focus:border-dark-green ekledim, focus olduğunda border da değişsin diye.
        })
    )
    email = forms.EmailField(
        label='E-posta Adresiniz',
        widget=forms.EmailInput(attrs={
            'placeholder': 'örnek@mail.com',
            # **Değişiklik:** Arka plan rengi eklendi (bg-gray-50) ve border rengi ayarlandı.
            'class': 'w-full px-4 py-2 bg-gray-50 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-dark-green focus:border-dark-green'
        })
    )
    subject = forms.CharField(
        max_length=200,
        label='Konu',
        widget=forms.TextInput(attrs={
            'placeholder': 'Konu',
            # **Değişiklik:** Arka plan rengi eklendi (bg-gray-50) ve border rengi ayarlandı.
            'class': 'w-full px-4 py-2 bg-gray-50 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-dark-green focus:border-dark-green'
        })
    )
    message = forms.CharField(
        label='Mesajınız',
        widget=forms.Textarea(attrs={
            'placeholder': 'Mesajınızı buraya yazın...',
            'rows': 6,
            # **Değişiklik:** Arka plan rengi eklendi (bg-gray-50) ve border rengi ayarlandı.
            'class': 'w-full px-4 py-2 bg-gray-50 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-dark-green focus:border-dark-green'
        })
    )