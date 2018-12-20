from flask import Flask, render_template

app = Flask(__name__, template_folder='static/templates/')

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/smash', methods=['POST'])
def smash():
    return

if __name__ == '__main__':
    app.debug = True
    app.run()
