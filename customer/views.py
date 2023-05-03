# Create your views here.
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from joblib import load
model = load('./savedModels/model.joblib')


@login_required
def customer_home(request):
    current_user = request.user
    print(current_user.id)
    context = {
        'name': current_user.first_name + " " + current_user.last_name
    }
    y_pred = model.predict([[10,20,10,30,40,40,50]])
    print(y_pred)
    return render(request, 'customer_home_page.html', {'context': context})

@login_required
def crop_prediction(request):
    if request.method == 'POST':
        n = int(request.POST.get('n'))
        p = int(request.POST.get('p'))
        k = int(request.POST.get('k'))
        rainfall = int(request.POST.get('rainfall'))
        ph = int(request.POST.get('ph'))
        temperature = int(request.POST.get('temperature'))
        humidity = int(request.POST.get('humidity'))

        y_pred = model.predict([[n, p, k, temperature, humidity, ph, rainfall]])
        print(y_pred)

    return render(request, 'customer_crop_prediction.html')

def log_out(request):
    logout(request)

    return HttpResponseRedirect('home.login_page')
