from django.shortcuts import render
from .forms import DepositForm
from django.http import JsonResponse
import requests
import json

def currency_converter(request):
    """
    Product search function using ajax
    """
    if request.is_ajax():
        res = None
        amount = request.POST.get('amount')
        reqUrl = "https://blockchain.info/tobtc?currency=USD&value="f'{amount}'

        headersList = {
        "Accept": "*/*",
        "User-Agent": "Thunder Client (https://www.thunderclient.io)" 
        }

        payload = ""

        response = requests.request("GET", reqUrl, data=payload,  headers=headersList)

        print(amount)
        btc = response.text

        if len(btc) > 0 :
            data = btc
            res = data
        else:
            res = 'Input an amount....'
        return JsonResponse({'data': res})

    return JsonResponse({})



def deposit (request):
    form = DepositForm(request.POST)
    context = {
        'form': form,
    }
    return render(request, 'user-pages/deposit.html', context)


def testing_api (request):

    url = "https://api.commerce.coinbase.com/charges"

    payload = json.dumps({
    "name": "Fund My Wallet",
    "description": "funding customers wallet ",
    "local_price": {
        "amount": "100.00",
        "currency": "USD"
    },
    "pricing_type": "fixed_price",
    "redirect_url": "https://charge/completed/page",
    "cancel_url": "https://charge/canceled/page"
    })
    headers = {
    'Content-Type': 'application/json',
    'X-CC-Api-Key': '1acd64ad-79cf-4d75-af31-b6f0e6004339',
    'X-CC-Version': '2018-03-22',
    'Cookie': 'amplitude_device_id=d3d09baa-9b9c-4830-8314-515623d6dfbf; coinbase_device_id=d3d09baa-9b9c-4830-8314-515623d6dfbf'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    # print(response.text)
    json_response = response.json()

    data = json_response['data']

    # jsonObject = json.dumps(data)

    # change the JSON string into a JSON object
    jsonObject = json.loads(response.text)

    # print the keys and values
    email = jsonObject['data']['addresses']['ethereum']
    return JsonResponse(email, safe=False)

