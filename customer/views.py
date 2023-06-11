# Create your views here.
from django.contrib import messages
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
def crop_prediction_result(request, n, p, k, t, h, ph, r):
    current_user = request.user
    temperature = t
    humidity = h
    rainfall = r

    y_pred = model.predict(
        [[float(n), float(p), float(k), float(temperature), float(humidity), float(ph), float(rainfall)]])
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


@login_required
def yield_prediction(request):
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
        # return redirect('customer_crop_prediction_result', n, p, k, temperature, humidity, ph, rainfall)

    return render(request, 'customer_yield_prediction.html', {'context': context})


@login_required
def weather(request):
    current_user = request.user
    context = {
        'name': current_user.first_name + " " + current_user.last_name
    }


    import requests
    from bs4 import BeautifulSoup

    if request.method == 'POST':
        city = request.POST.get('city')

        try:
            # creating url and requests instance
            url = "https://www.google.com/search?q=" + "weather" + city
            html = requests.get(url).content

            # getting raw data
            soup = BeautifulSoup(html, 'html.parser')
            temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
            str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text


            # formatting data
            data = str.split('\n')
            print(data)
            time = data[0]
            sky = data[1]

            # getting all div tag
            listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
            strd = listdiv[5].text

            # getting other required data
            pos = strd.find('Wind')
            other_data = strd[pos:]

            # printing all data
            print("Temperature is", temp)
            print("Time: ", time)
            print("Sky Description: ", sky)
            print(other_data, type(other_data))
            # Python code to display schematic weather details


            # import requests
            # # Sending requests to get the IP Location Information
            # res = requests.get('https://ipinfo.io/')
            # # Receiving the response in JSON format
            # data = res.json()
            # # Extracting the Location of the City from the response
            # # citydata = data['city']
            # citydata = city
            # # Prints the Current Location
            # print(citydata)
            # # Passing the City name to the url
            # url = 'https://wttr.in/{}'.format(citydata)
            # # Getting the Weather Data of the City
            # res = requests.get(url)
            # # Printing the results!
            # print(res.next)
            #
            # # This code is contributed by PL VISHNUPPRIYAN

            context = {
                'name': current_user.first_name + " " + current_user.last_name,
                'temp': temp,
                'time': time,
                'sky': sky,
                'city': city,
                'others': other_data

            }
            return render(request, 'customer_weather_page.html', {'context': context})

        except:
            messages.error(request, 'Please enter correct city name')

    return render(request, 'customer_weather_page.html', {'context': context})


def fertilizer_suggestion(request):

    return render(request, 'customer_fertilizer_suggestion.html')

def weather_result(request, city):


    return render(request, 'customer_weather_page_result.html', )




def log_out(request):
    logout(request)

    return HttpResponseRedirect('home.login_page')
