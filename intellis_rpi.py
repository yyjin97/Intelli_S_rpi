import json
import sys
from websocket import create_connection
import paho.mqtt.client as mqtt 

address = ""
port = ""
json_send = "{\"bno\":[0,1,2]}"


def connect_server():
    try:
        ws = create_connection("ws://"+address+":"+port+"/rpi")
        print("connect to " + address + ":" + port)
        ws.send(json_send)
    except Exception as e:
        print(e)
        ws.close()
        exit()

    mqt = mqtt.Client("mypub")
    mqt.connect("localhost",1883)
    while True:
        result = ws.recv()
        bno, rno = result.split(',')
	if bno=="0" and rno=="0":
	    mqt.publish('motor', 1)
	elif bno=="0" and rno=="1":
	    mqt.publish('motor',2)
	elif bno=="0" and rno=="2":
	    mqt.publish('motor',3)
	elif bno=="1" and rno=="0":
	    mqt.publish('motor',4)
	print("The message is published.")
        print("open bno:" + bno + " rno:" + rno) 
        mqt.loop(2)
    ws.close()

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: " + sys.argv[0] + " address port")
        exit()
    address = sys.argv[1]
    port = sys.argv[2]
    connect_server()
