from django.shortcuts import render, redirect
from .forms import ContactForm
from django.urls import reverse
from django.core.mail import EmailMessage
# Create your views here.

def contactos(request):
    contact_form = ContactForm()
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name','')
            email = request.POST.get('email','')
            content = request.POST.get('content','')
            #Enviamos correo y redireccionamos
            email = EmailMessage(
                "La Caffeteria: Nuevo cafe turco",
                f"DE {name} <{email}>\n\nEscribio:\n\n{content}",
                "no_reply@inbox.mail.io",
                ['franco.manfredi2006@gmail.com'],
                reply_to=[email]
            )
            try:
                email.send()
                return redirect(reverse('contactos')+"?ok")
            except:
                return redirect(reverse('contactos')+"?fail")
            
    return render(request,"contact/contact.html",{'form':contact_form})
