from django.contrib import messages
from django.shortcuts import render, redirect

import customer.views
from login.models import User


# Create your views here.
def login_page(request):
    # r = "linkedin"
    # print(r[4:-4])
    if request.method == 'POST':
        username1 = request.POST.get('username')
        password1 = request.POST.get('password')

        user = User.objects.get(username=username1, password=password1, is_active = True)
        if user:
            #  print(i.username, i.password)
            first_name = user.first_name
            last_name = user.last_name
            # full_name = first_name +" "+ last_name
            # request.session['name'] = full_name
            # request.session['status'] = 1
            # request.session['hod_username'] = username1



            return redirect('customer_home')



        else:
            messages.error(request, 'Invalid username or password')
            return render(request, 'login.html')

    return render(request, 'login.html')
