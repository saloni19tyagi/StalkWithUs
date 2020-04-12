from django.shortcuts import redirect,render
from .forms import UserRegistrationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from .models import userdata

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            if request.POST.get('password') != request.POST.get('confirm_password'):
                messages.error(request, f'Password Does not match!')
            else:
                form.first_name = request.POST.get('first_name')
                form.last_name = request.POST.get('last_name')
                form.email = request.POST.get('email')
                form.password = request.POST.get('password')
                form.institute = request.POST.get('institute')
                form.handle = request.POST.get('handle')
                form.codechef = request.POST.get('codechef')
                form.codeforces = request.POST.get('codeforces')
                form.hackerrank = request.POST.get('hackerrank')
                form.hackerearth = request.POST.get('hackerearth')
                form.spoj = request.POST.get('spoj')
                form.linkedin = request.POST.get('linkedin')
                form.github = request.POST.get('github')
                form.save()
                messages.success(request, f'Account created!')
        else:
            print(form.errors)
            messages.error(request, f'Error')
    else:
        form = UserRegistrationForm()

    return render(request, 'registration/register.html', {'form': form})
