
# import logging

from flask import Flask,  request, render_template, jsonify
from google.cloud import translate

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def landing_page():
    if request.method == 'POST':
        if request.form['submit_button'] == 'Translate':
            text_input = request.form['text']
            client = translate.Client()
            translate_dict = client.translate(text_input)
            return jsonify(translate_dict)
        elif request.form['submit_button'] == 'Detect':
            text_input = request.form['text']
            client = translate.Client()
            detect_dict = client.detect_language(text_input)
            return jsonify(detect_dict)
        else:
            pass
    return render_template('index.html')


@app.route('/translate', methods=['GET', 'POST'])
def translate_language():
    if request.method == 'POST':
        text_input = request.form['text']
        client = translate.Client()
        translate_dict = client.translate(text_input)
        # return redirect(url_for('index'))
        return jsonify(translate_dict)
    return render_template('translate.html')


@app.route('/detect', methods=['GET', 'POST'])
def detect_language():
    if request.method == 'POST':
        text_input = request.form['text']
        client = translate.Client()
        detect_dict = client.detect_language(text_input)
        return jsonify(detect_dict)
    return render_template('detect.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
