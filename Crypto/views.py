from django.shortcuts import render

# Create your views here.

def home(request):
    import requests #use requests module(use pip3 to install json)
    import json #use json module (use pip3 to install json)

    #Retrive news data
    news_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")#get news api from site
    api1 = json.loads(news_request.content)# convert api content to json

    #Retrive price data
    price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,XRP,ETH,EOS,LTC,QTUM,ZEC,ETC&tsyms=USD,EUR")#get price api from site
    price_api = json.loads(price_request.content)# convert api content to json

    return render(request, 'index.html', {'api': api1, 'price':price_api})


def prices(request):
        #this a functionality to search through the api for info. on coins on the prices.html page

       #Retrive price data
    if request.method == 'POST': #if it gets request.method from html
        import requests #use requests module(use pip3 to install json)
        import json #use json module (use pip3 to install json)

        search1 = request.POST['search'] #coin search from the search input
        search1 = search1.upper() #convert any input to capital
        search_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms="+search1+"&tsyms=USD")
        search_output = json.loads(search_request.content)# convert api content to json
        return render(request, 'prices.html', {'search': search1, 'searchoutput': search_output})
    else:
        return render(request, 'prices.html', {})


