# settingsService
For the OSU CS361 project, I have created a microservice to handle loading and saving settings for an app using JSON. Using zeroMQ as a local server, the settingsService microservice can be run similarly to other python files (for example in the Command prompt):

```
python settingsService.py
```
### Service setup
While using the zeroMQ library, the setup on the client side using python would be:
```
context = zmq.Context()
print("Connecting to CS361 microservice server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")
```

The setup for the microservice using python would be:
```
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")
```

### Request data 
Two different types of requests can be made to the settingsService. The first option is to send a request to load the current settings. To do this, the client can send a string of 'load' using :
```
socket.send_string('load')
```
The other option is to save new settings. To do this, the client side would need a new JSON object with the new values of the settings. The client can send the JSON object like this:
```
new_settings = {
    "background-color":"Black",
    "number-columns": 10,
    "number-rows":10,
    "row-column-display-numbers": True,
    "size-of-numbers": 10,
    "number-color": "White",
    "correct-outline": True,
    "outline-color": "Blue",
    "outline-size": 10,
    "invert-controls": True,
    "show-hint": True,
    "empty-box-location": True 
}

socket.send_json(new_settings)

```
Once the new_settings JSON is sent to the microservice, the settings JSON file is updated. The microservice does not send any data back, but processes the received data.

### Receive data
Once the client sends the 'load' string, the microservice will receive the string like this:
```
message = socket.recv()
```
After the 'load' string is received, the microservice will process the current JSON file settings and then send the current JSON file settings like this:
```
socket.send_json(json_object)
```

and the client should receive the current settings like this:
```
json_object = socket.recv()
```
The JSON object the client receives would looke like this:
```
{

    "background-color":"white",

    "number-columns": 5,

    "number-rows":5,

    "row-column-display-numbers": false,

    "size-of-numbers": 5,

    "number-color": "Black",

    "correct-outline": false,

    "outline-color": "Yellow",

    "outline-size": 5,

    "invert-controls": false,

    "show-hint": false,

    "empty-box-location": false

}
```

### UML Diagram

![UML_SettingsService](https://user-images.githubusercontent.com/94848858/236927242-a98bd131-d127-44dd-ba1f-36e4debeda4e.png)

