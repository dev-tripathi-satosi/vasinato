from flask import Flask, render_template
import json
import requests
#from threading import Thread
app = Flask(__name__)
from flask import request
from flask import jsonify
from pymongo import MongoClient
#client = MongoClient('mongodb+srv://satosi:<satosi>@cluster0.qnronfw.mongodb.net/?retryWrites=true&w=majority')
#db = client['website']
client = MongoClient("mongodb+srv://satosi:satosi@cluster0.qnronfw.mongodb.net/?retryWrites=true&w=majority")
db = client.website
data = db.wmail
req = db.botreq 

@app.route('/',methods=('GET', 'POST'))
def mainf():
  return render_template('index.html')

@app.route('/handle_data',methods=('GET', 'POST'))
def handle_data():
  if request.method=='POST': 
    name = request.form['name'] 
    email = request.form['email']
    subject = request.form['subject'] 
    message = request.form['message'] 
    data.insert_one({'name': name, 'email': email,'subject':subject,'message':message}) 
    return render_template('index.html')
  all_data = data.find()



@app.route('/load_data',methods=('GET', 'POST'))
def load_data():
  if request.method=='POST': 
    name = request.form['name'] 
    email = request.form['email']
    dcID = request.form['dcID'] 
    token = request.form['token']
    bstatus = request.form['bstatus']
    comment = request.form['comment']
    req.insert_one({'name': name, 'email': email,'discord ID':dcID,'token':token,'bstatus':bstatus}) 
    return render_template('bot.html')

@app.route('/bot/')
def DiscordBot():
    return render_template('bot.html')

@app.route('/TC/')
def TC():
    return render_template('T&C.html')


app.route("/get_my_ip", methods=["GET"]) 
def get_my_ip(): 
  return jsonify({'ip': request.remote_addr}), 200


@app.route('/bots/cmds/')
def cmds():
  return render_template('cmds.html')

@app.route('/about/')
def about():
  return render_template('about.html')

@app.errorhandler(404)
def pagenotfound(e):
 return render_template('404.html')

@app.route('/UD/')
def UD():
    return render_template('underdevelopment.html')

app.run(host='0.0.0.0', port=8080)
