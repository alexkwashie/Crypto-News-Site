from django.shortcuts import render

# Create your views here.

def home(request):
    import requests #use requests module(use pip3 to install json)
    import json #use json module (use pip3 to install json)
    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")#get api from site
    api1 = json.loads(api_request.content)# convert api content to json
    return render(request, 'index.html', {'api': api1})
