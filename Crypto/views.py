from django.shortcuts import render

# Create your views here.

def home(request):
    import requests # this allows us to call for reqest form webpage(use pip3 install to use)
    import json # allows us to work with the API objects
    api_request = request.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.load(api_request.content)
    return render(request, 'index.html', {})
