# This example uses Python 2.7 and the python-request library.

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from twilio.rest import Client

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'
parameters = {
    'start': '1',
    'symbol': 'FET',
    'limit': '1'
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '',
}

session = Session()
session.headers.update(headers)

try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)

coin_name = data['data'][0]['name']
id = data['data'][0]['id']
print(id)
print(coin_name)

account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)


message = client.messages.create(
  from_='+18884027213',
  body="CHECK YOUR " + coin_name,
  to=''
)

print(message.sid)
