from django.shortcuts import render
import requests
import datetime
from django.contrib import messages

def home(request):

    if 'city' in request.POST:
        city=request.POST['city']
    else:
        city='moscow'

    url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=85965c92ee00f13c1755de3c235e2747'
    PARAMS={'units':'metric'}

    API_KEY='AIzaSyAlvKJmO3Zytg4TiXEibx4bFQkIGyHSt_c'
    SEARCH_ENGINE_ID='2678285f833484248'


    query = city + " 1920x1080"
    page = 1
    start = (page - 1) * 10 + 1
    searchType = 'image'
    city_url=f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&searchType={searchType}&imgSize=xlarge"


    data = requests.get(city_url).json()
    count = 1
    search_items = data.get("items")
    image_url = search_items[1]['link']

    try:
        data=requests.get(url,PARAMS).json()

        description=data['weather'][0]['description']
        icon=data['weather'][0]['icon']
        temp=data['main']['temp']

        day=datetime.date.today()


        return render(request,'weather/index.html',{'description':description,'icon':icon,
                                                    'temp':temp,'day':day,'city':city,
                                                    'exception_occured':False,'image_url':image_url})
    except KeyError:
        exception_occured=True
        messages.error(request,'entered data is not avaliable API')
        day=datetime.date.today()

        return render(request,'weather/index.html',{'description':'clear sky','icon':'01d',
                                                    'temp':25,'day':day,'city':'moscow',
                                                    'exception_occured':exception_occured})



   

