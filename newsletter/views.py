from django.shortcuts import render


# Create your views here.
from newsletter.forms import SignUpForm


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
