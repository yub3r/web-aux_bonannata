from django import forms


class ContactForm(forms.Form):
    nombre = forms.CharField(max_length=100, label='Nombre')
    email = forms.EmailField(label='Email')
    telefono = forms.CharField(max_length=30, required=False, label='Teléfono')
    mensaje = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}), label='Mensaje')
