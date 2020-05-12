import paho.mqtt.client as mqtt
import random
# Define event callbacks
def on_connect(client, userdata, flags, rc):
    print("rc: " + str(rc))

def on_message(client, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

def on_publish(client, obj, mid):
    print("mid: " + str(mid))

def on_subscribe(client, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_log(client, obj, level, string):
    print(string)

client = mqtt.Client()
# Assign event callbacks
client.on_message = on_message
client.on_connect = on_connect
client.on_publish = on_publish
client.on_subscribe = on_subscribe


topic = 'temperatur'

# Connect mqtt ke server
client.username_pw_set('krlahobw', 'NIbqe3aleMsE')
client.connect('tailor.cloudmqtt.com', 15527)

rc = 0
while rc == 0:
    data = random.randint(24,32)
    client.publish(topic, data)




