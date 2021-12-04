currency_in = 'USD'
currency_out = 'NOK'
import urllib.request
req = urllib.request.urlopen('https://finance.yahoo.com/d/quotes.csv?e=.csv&f=sl1d1t1&s='+currency_in+currency_out+'=X')
result = req.read()