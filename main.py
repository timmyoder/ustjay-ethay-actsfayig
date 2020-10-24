import os

import requests
from flask import Flask, send_file, Response
from bs4 import BeautifulSoup

app = Flask(__name__)


def get_fact():

    response = requests.get("http://unkno.com")

    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    return facts[0].getText()


@app.route('/')
def home():
    fact = get_fact()
    pig_url = 'https://hidden-journey-62459.herokuapp.com'
    data = {'input_text': fact}
    response = requests.post(f'{pig_url}/piglatinize/',
                             data,
                             allow_redirects=False)
    soup = BeautifulSoup(response.content, 'html.parser')
    result = soup.find_all('a')[0].getText()
    result_url = f'{pig_url}{result}'
    clickable = f'<a href="{result_url}">{result_url}</a>'
    return clickable


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)

