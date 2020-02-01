
# import logging

from flask import Flask
from flask import jsonify
from time import gmtime, strftime
from google.cloud import translate


app = Flask(__name__)


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello I like to make AI Apps'


@app.route('/name/<value>')
def name(value):
    val = {"value": value}
    return jsonify(val)


@app.route('/html')
def html():
    """Returns some custom HTML"""
    return """
    <title>This is a Hello World World Page</title>
    <p>Hello</p>
    <p><b>World</b></p>
    """


@app.route('/time')
def time():
    my_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    print("This was the time I returned")
    my_time_dict = {"time": my_time}
    return jsonify(my_time_dict)


@app.route('/translate')
def translate_language():
    text_input = 'koszula'
    client = translate.Client()
    translate_dict = client.translate(text_input)
    return jsonify(translate_dict)


@app.route('/detect')
def detect_language():
    text_input = 'Me llamo'
    client = translate.Client()
    detect_dict = client.detect_language(text_input)
    return jsonify(detect_dict)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
