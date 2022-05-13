# -----------------------------------------------------------------------------
# imports for connecting to mosquitto
# -----------------------------------------------------------------------------
import paho.mqtt.client as mqttclient
from queue import Queue
import json
import pdb

connected = False
broker_address = "localhost"
port = 1883
# ------------------
user = "sng"
password = "sng123"
# ------------------
client_name = 'MQTT'
sub_topic = 'sng/db'
pub_topic = 'sng/test'
# ------------------


class MQTTClient:
    def __init__(self, db, cname=client_name):
        self.db = db
        self.name = cname
        self.client = mqttclient.Client(cname)
        self.client.username_pw_set(user, password=password)
        self.client.on_connect = self.on_connect
        self.client.on_disconnect = self.on_disconnect
        self.client.on_message = self.on_message
        self.client.on_publish = self.on_publish
        self.client.connect(broker_address, port)

        self.q = Queue()

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:  # okay
            print("1:client is connected")
        else:
            print("1:Connection failed")

    def on_message(self, client, userdata, message):
        # pdb.set_trace()
        msg = str(message.payload.decode("utf-8"))
        print("1:Message received: " + msg)
        print("1:Topic: " + str(message.topic))
        # self.q.put(msg)

    def on_publish(self, client, data, result):
        print("1:data published")

    def on_disconnect(self, client, userdata, rc):
        print("1:client disconnected ok")

    def subscribe(self, topic=sub_topic):
        self.client.subscribe(topic)

    def publish(self, msg_dict, topic=pub_topic):
        msg = json.dumps(msg_dict)
        ret = self.client.publish(topic, msg)
        return ret

    def start(self):
        self.client.loop_start()

    def stop(self):
        self.client.loop_stop()
