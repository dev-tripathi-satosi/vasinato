from flask import Flask, render_template
#from threading import Thread
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')

    
    


@app.route('/product')
def products():
    return "products"


app.run(host='0.0.0.0', port=8080)
