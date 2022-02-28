
#https://levelup.gitconnected.com/deploy-your-first-flask-mongodb-app-on-kubernetes-8f5a33fa43b4

from flask import Flask, request, jsonify, render_template, make_response, send_from_directory
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import socket


#TODO: Configure Flask
app = Flask(__name__)



#TODO: Make PWA
@app.route('/sw.js')
def service_worker():
    response = make_response(send_from_directory('static', 'sw.js'))
    response.headers['Cache-Control'] = 'no-cache'
    return response

@app.route('/manifest.json')
def manifest():
    return app.send_from_directory('static', 'manifest.json')
  
@app.route('/favicon.ico')
def favicon():
    return app.send_from_directory('static', 'favicon.ico')
# END PWA


#TODO: API Routes
@app.route("/")
def index():
    hostname = socket.gethostname()
    message="I am running inside {} pod!".format(hostname)
    return render_template('index.html', message=message)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)