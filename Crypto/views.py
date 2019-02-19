from django.shortcuts import render

# Create your views here.

def home(request):
    import requests #use requests module(use pip3 to install json)
    import json #use json module (use pip3 to install json)

    #Retrive news data
    news_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")#get news api from site
    api1 = json.loads(news_request.content)# convert api content to json

    #Retrive price data
    price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,XRP&tsyms=USD,EUR")#get price api from site
    price_api = json.loads(price_request.content)# convert api content to json

    return render(request, 'index.html', {'api': api1,'price':price_api})
