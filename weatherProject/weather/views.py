from django.shortcuts import render
import requests
import datetime

def home(request):

    if 'city' in request.POST:
        city=request.POST['city']
    else:
        city='moscow'

    url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=85965c92ee00f13c1755de3c235e2747'
    PARAMS={'units':'metric'}


    data=requests.get(url,PARAMS).json()

    description=data['weather'][0]['description']
    icon=data['weather'][0]['icon']
    temp=data['main']['temp']

    day=datetime.date.today()


    return render(request,'weather/index.html',{'description':description,'icon':icon,
                                                'temp':temp,'day':day,'city':city})

