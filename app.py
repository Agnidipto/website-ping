from re import A
import requests

a = requests.get('http://dewalisinha.com')
b = requests.get('https://house-price-react.herokuapp.com')
c = requests.get('https://apartment-backend-flask.herokuapp.com/get_location_names')
d = requests.get('https://staying-together.herokuapp.com')
e = requests.get('https://dewali-sinha.herokuapp.com/test/users')

print(b)