import os
from flask import Flask, render_template, request, jsonify, send_from_directory

from modules import hammer

app = Flask(__name__, template_folder='static/templates/')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico')


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/smash', methods=['POST'])
def smash():
    req_body = request.values
    url = req_body['url']
    params = req_body['args']
    ctrl = req_body['ctrl_group']
    method = request.method

    result = hammer.smash(url, params, ctrl, method)
    return jsonify(result)


@app.route('/health_check', methods=['GET', 'POST'])
def health_check():
    response = {
        'message': 'Success'
    }

    if request.method == 'GET':
        return jsonify(response)
    elif request.method == 'POST':
        body = request.values
        response['body'] = body
        return jsonify(response)


if __name__ == '__main__':
    app.debug = True
    app.run()
