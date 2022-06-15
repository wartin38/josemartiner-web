from django import forms

class ContactForm(forms.Form):
  nombre = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Nombre', 'class': 'form-nombre'}))
  mensaje = forms.CharField(max_length=350, widget=forms.Textarea(attrs={'placeholder': 'Mensaje', 'class': 'form-texto'}))
  correo_e = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Tu correo', 'class': 'form-correo'}))
