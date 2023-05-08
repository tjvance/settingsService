import time
import zmq
import json


context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    message = socket.recv()
    if type(message) == bytes:
        message = message.decode()
    # Check to see what message was sent
    print(message)
    if message == "load":
        with open("settings.json", "r") as read_file:
            settings = read_file.read()
            data = json.loads(settings)        
    else:
        print(type(message))
        with open("settings.json", "w") as write_file:
            new_json_settings = json.loads(message)
            json.dump(new_json_settings, write_file)
            message = 'save'
            data = new_json_settings
    print("Received request: %s" % message)
    json_object = json.dumps(data)
    socket.send_json(json_object)