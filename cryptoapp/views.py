from django.shortcuts import render

# Create your views here.
def home(request):
    import requests
    import json
    # Crypto Prices
    price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,XRP,TRX,BCH,USDT&tsyms=USD")
    price = json.loads(price_request.content)
    # Crypto News
    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_request.content)

    return render(request, 'home.html', {'api': api, 'price': price})


def prices(request):
    if request.method == 'POST':
        import requests
        import json
        qoute = request.POST['qoute']
        qoute = qoute.upper()
        crypto_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + qoute + "&tsyms=USD")
        crypto = json.loads(crypto_request.content)
        return render(request, 'prices.html',{'qoute': qoute, 'crypto': crypto})

    else:
        notfound = print("Please Enter a crypto abbreviation in the form above")
        return render(request, 'prices.html',{'notfound': notfound})
