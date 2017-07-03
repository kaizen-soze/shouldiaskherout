from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/user/<rawr>', defaults = {'rawr': None})
def user(rawr):
    print('Rawr is {0}'.format(rawr))
    return render_template('name.html', name=rawr)

if __name__ == "__main__":
    application.run(host='0.0.0.0')