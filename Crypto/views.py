from django.shortcuts import render

# Create your views here.

api2 = ''

def home(request):
    import requests #use requests module(use pip3 to install json)
    import json #use json module (use pip3 to install json)
    import html

    #Retrive news data
    news_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")#get news api from site

    api1 = json.loads(news_request.content)# convert api content to json

    api_body = api1['Data'][1]['body']

    global api2
    api2 = api1['Data'][1]

    #Retrive price data
    price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,XRP,ETH,EOS,LTC,XMR,ZEC,ETC,REP,BSV&tsyms=USD,EUR")#get price api from site
    price_api = json.loads(price_request.content)# convert api content to json

    return render(request, 'index.html', {'api': api1, 'price':price_api, 'api2':api2})


def prices(request):
#this a functionality to search through the api for info. on coins on the prices.html page

       #Retrive price data
    if request.method == 'POST': #if it gets request.method from html
        import requests #use requests module(use pip3 to install json)
        import json #use json module (use pip3 to install json)

        api3 = api2

        search1 = request.POST['search'] #coin search from the search input
        search1 = search1.upper() #convert any input to capital
        quote = request.POST['search']
        search_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms="+search1+"&tsyms=GBP")
        search_output = json.loads(search_request.content)# convert api content to json

        return render(request, 'prices.html', {'searchoutput': search_output, 'quote': quote,})

    else:
        notfound = "Please enter crypto code in the search field to view info. eg. BTC for bitcoin or ETH for Ethereum"
        return render(request, 'prices.html', {'notfound1': notfound})


