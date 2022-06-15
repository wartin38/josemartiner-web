from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ContactForm
from django.core.mail import send_mail

def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            mensaje = form.cleaned_data['mensaje']
            correo_e = form.cleaned_data['correo_e']

            mensaje = ' '.join([mensaje, correo_e])

            mi_correo = 'josemartiner1@outlook.com'

            recipients = ['martinesre@gmail.com']

            send_mail(nombre, mensaje, mi_correo, recipients)
            return HttpResponseRedirect('/gracias/')
    else:
        form = ContactForm()

    return render(request, 'landing/home.html', {"form": form})


def gracias(request):
    return render(request, 'landing/gracias.html')
