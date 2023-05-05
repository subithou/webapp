# Create your views here.
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from joblib import load

model = load('./savedModels/model.joblib')


@login_required
def customer_home(request):
    current_user = request.user
    print(current_user.id)
    context = {
        'name': current_user.first_name + " " + current_user.last_name
    }
    y_pred = model.predict([[10, 20, 10, 30, 40, 40, 50]])
    print(y_pred)
    return render(request, 'customer_home_page.html', {'context': context})


@login_required
def crop_prediction(request):
    current_user = request.user
    context = {
        'name': current_user.first_name + " " + current_user.last_name
    }

    if request.method == 'POST':
        n = float(request.POST.get('n'))
        p = float(request.POST.get('p'))
        k = float(request.POST.get('k'))
        rainfall = float(request.POST.get('rainfall'))
        ph = float(request.POST.get('ph'))
        temperature = float(request.POST.get('temperature'))
        humidity = float(request.POST.get('humidity'))

        print(n, p, k, temperature, humidity, ph, rainfall)
        return redirect('customer_crop_prediction_result', n, p, k, temperature, humidity, ph, rainfall)

    return render(request, 'customer_crop_prediction.html', {'context': context})


@login_required
def crop_prediction_result(request, n, p, k, t,h,ph,r ):
    current_user = request.user


    temperature = t
    humidity = h
    rainfall = r

    y_pred = model.predict([[float(n), float(p), float(k), float(temperature), float(humidity), float(ph), float(rainfall)]])
    print(y_pred[0])
    context = {
        'crop': y_pred[0].upper(),
        'n': n,
        'p': p,
        'k': k,
        'temperature': temperature,
        'rainfall': rainfall,
        'humidity': humidity,
        'ph': ph,
        'name': current_user.first_name + " " + current_user.last_name
    }
    return render(request, 'customer_crop_prediction_result.html', {'context': context})


def log_out(request):
    logout(request)

    return HttpResponseRedirect('home.login_page')
