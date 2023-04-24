from django.contrib import messages
from django.shortcuts import render, redirect

from login.models import User


# Create your views here.

def home_page(request):
    return render(request, 'homePage.html')


def login_page(request):
    if request.method == 'POST':
        username1 = request.POST.get('username')
        password1 = request.POST.get('password')
        try:
            user = User.objects.get(username=username1, password=password1, is_active=True)
            if user:
                return redirect('customer_home')

        except:
            messages.error(request, 'Invalid username or password')
            return render(request, 'loginPage.html')

    return render(request, 'loginPage.html')
