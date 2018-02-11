from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
from newsletter.forms import SignUpForm, ContactForm


def home(request):
    form = SignUpForm(request.POST or None)

    context = {
        'form': form,
        'title': 'Welcome to Sign Up Page'
    }

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        print(instance)

        context = {
            'title': 'Thank You :)'
        }

    return render(request, "home.html", context)


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form_email = form.cleaned_data.get('email')
        form_message = form.cleaned_data.get('message')
        form_full_name = form.cleaned_data.get('full_name')
        subject = 'Site contact Form'
        from_email = settings.EMAIL_HOST_USER
        to_email = ['dangi.sushil5@gmail.com', 'sushil@pacdevelopers.com']
        contact_message = '%s : %s via %s' % (form_email, form_message, form_full_name)
        send_mail(subject,
                  contact_message,
                  from_email,
                  to_email,
                  fail_silently=False)

    context={
        'form':form,
    }
    return render(request,'forms.html',context)