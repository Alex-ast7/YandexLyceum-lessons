import json

from flask import render_template, Flask

app = Flask(__name__)

@app.route('/')
@app.route('/index/<new_title>')
def index(new_title):
    return render_template('index.html', title=new_title)

@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', prof=prof)



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')