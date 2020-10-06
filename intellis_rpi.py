import json
import sys
from websocket import create_connection

address = ""
port = ""
json_send = "{\"bno\":[1,2]}"

def connect_server():
    try:
        ws = create_connection("ws://"+address+":"+port+"/rpi")
        print("connect to " + address + ":" + port)
        ws.send(json_send)
    except Exception as e:
        print(e)
        ws.close()
        exit()
    while True:
        result = ws.recv()
        bno, rno = result.split(',')
        ###############
        print("open bno:" + bno + " rno:" + rno) 
    ws.close()

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: " + sys.argv[0] + " address port")
        exit()
    address = sys.argv[1]
    port = sys.argv[2]
    connect_server()
