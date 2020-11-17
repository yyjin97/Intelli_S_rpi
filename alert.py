import paho.mqtt.client as mqtt
import time
import sys
import json
import requests

broker = "localhost"
def on_message(client,userdata,message):
    time.sleep(1)
    recvData = str(message.payload.decode("utf-8"))
    print(recvData)
    dictData = json.loads(recvData)
    if dictData["temp"] > 1000:
        print("FIRE!!!!!!!!!!!!!!!!!")
        requests.get("http://192.168.137.1:8080/fire")

def connect_aduino():
    mqt = mqtt.Client()
    mqt.on_message=on_message

    while True:
        mqt.connect(broker, 1883)
        mqt.loop_start()
        mqt.subscribe("temp")
        time.sleep(3)
        mqt.disconnect()
        mqt.loop_stop()
        time.sleep(3)


if __name__ == '__main__':
    connect_aduino()
