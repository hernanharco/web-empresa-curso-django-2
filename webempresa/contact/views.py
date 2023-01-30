from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm


# Create your views here.
def contact(request):
    # print('Tipo de petición: {}'.format(request.method))
    contact_form = ContactForm()

    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('contect', '')
            # Enviamos el correo y redireccionamos
            email = EmailMessage(
                'La caffettiera: Nuevo mensaje de contacto',
                'De {} <{}>\n\nEscribió:\n\n{}'.format(name, email, content),
                'no-contestar@inbox.mailtrap.io',
                ['django@hernan.harco.net'],
                reply_to=[email]
            )

            try:
                email.send()
                # Suponemos que todo ha ido bien, redireccionamos
                return redirect(reverse('contact')+'?ok')
            except Exception as ex:
                # Algo no ha ido bien, redireccionamos a FAIL
                return redirect(reverse('contact')+'?fail')

    return render(request, 'contact/contact.html', {'form': contact_form})
