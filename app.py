from re import A
import requests

a = requests.get('http://dewalisinha.com')
b = requests.get('https://house-price-react.herokuapp.com')
c = requests.get('https://apartment-backend-flask.herokuapp.com/get_location_names')

print(b)