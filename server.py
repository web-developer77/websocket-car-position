from flask import Flask, request,jsonify
from flask_socketio import SocketIO,emit
from flask_cors import CORS
import json
import time
import sqlite3
import paho.mqtt.client as paho
from paho import mqtt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
CORS(app,resources={r"/*":{"origins":"*"}})
socketio = SocketIO(app,cors_allowed_origins="*")

@app.route("/http-call")
def http_call():
    """return JSON with string data as the value"""
    data = {'data':'This text was fetched using an HTTP call to server on render'}
    return jsonify(data)

@socketio.on("connect")
def connected():
    """event listener when client connects to the server"""
    print(request.sid)
    print("client has connected")
    emit("connect",{"data":f"id: {request.sid} is connected"})

@socketio.on('data')
def handle_message(data):
    """event listener when client types a message"""
    print("data from the front end: ",str(data))
    emit("data",{'data':data,'id':request.sid},broadcast=True)

@socketio.on("disconnect")
def disconnected():
    """event listener when client disconnects to the server"""
    print("user disconnected")
    emit("disconnect",f"user {request.sid} disconnected",broadcast=True)

    # setting callbacks for different events to see if it works, print the message etc.
# def on_connect(client, userdata, flags, rc, properties=None):
#     print("CONNACK received with code %s." % rc)

# # with this callback you can see if your publish was successful
# def on_publish(client, userdata, mid, properties=None):
#     print("mid: " + str(mid))

# # print subscribed if the client successfully subscribes to the topic
# def on_subscribe(client, userdata, mid, granted_qos, properties=None):
#     print("Subscribed: ")

# # print message, useful for checking if it was successful
# def on_message(client, userdata, msg):
#     conn = sqlite3.connect('D:/03_projects/websocket-car-position/db/projectDatabase.db')
#     c = conn.cursor()

#     my_json = msg.payload.decode('utf8').replace("'", '"')
#     data = json.loads(my_json)
#     print(data)
    
#     c.execute("INSERT INTO mqttData VALUES(?,?,?,?,?,?,?,?,?,?)",(None,data["lon"],data["lat"],None,data["azimuth"],data["time"],data["devId"],data["satelitesError"],data["satelites"],data["softVersion"]))
#     conn.commit()
#     conn.close()
    
# # using MQTT version 5 here, for 3.1.1: MQTTv311, 3.1: MQTTv31
# # userdata is user defined data of any type, updated by user_data_set()
# # client_id is the given name of the client
# client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)
# client.on_connect = on_connect

# # enable TLS for secure connection
# client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
# # set username and password
# client.username_pw_set("monitoring_app02", "KZ8O0IWTR1GVv9dKGyfAHUeGc")
# # connect to HiveMQ Cloud on port 8883 (default for MQTT)
# client.connect("48d783a6e5c64bacbb580974e318d60d.s1.eu.hivemq.cloud", 8883)

# # setting callbacks, use separate functions like above for better visibility
# client.on_subscribe = on_subscribe
# client.on_message = on_message
# #client.on_publish = on_publish

# # subscribe to topic
# client.subscribe("/sx/")

if __name__ == '__main__':
    socketio.run(app, debug=True,port=5001)
