from flask import Flask
import requests

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/weather/<city>')
def weather(city):
    secret = '59a56cadf932516f889c66827be02f40'
    url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'q': city, 'units': 'metric', 'appid': secret}
    response = requests.get(url=url, params=params)
    temperature = str(response.json()['main']['temp'])

    secret_gif = 'KAdHlVWzEBrP75xwpYOf1ug9ddJlYOAg'
    url_gif = 'http://api.giphy.com/v1/gifs'

    if float(temperature) < 10:
        giff = 's4Bi420mMDRBK'
    elif float(temperature) < 18:
        giff = 'X4M6homF66qFq'
    else:
        giff = '5xtDarIN81U0KvlnzKo'

    params = {'ids': giff, 'api_key': secret_gif}
    response = requests.get(url=url_gif, params=params)
    gif_url = str(response.json()['data'][0]['images']['original']['url'])
    pic = "<br><img src=" + gif_url + ">"
    return 'Temperature in ' + city + ' is:' + temperature + pic


if __name__ == "__main__":
    app.run()
