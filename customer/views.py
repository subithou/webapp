# Create your views here.

from django.shortcuts import render


def customer_home(request):
    return render(request, 'customer_home_page.html')

