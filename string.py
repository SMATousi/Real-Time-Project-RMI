'''
This process is supposed to control the robotic arm
to play the string and make the sound.

'''

import sys
import zmq
import json

port = "5556"
if len(sys.argv) > 1:
    port =  sys.argv[1]
    int(port)
    
if len(sys.argv) > 2:
    port1 =  sys.argv[2]
    int(port1)

# Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)

socket.setsockopt(zmq.SUBSCRIBE, b'')

print ("Collecting updates from weather server...")
socket.connect("tcp://localhost:%s" % port)

if len(sys.argv) > 2:
    socket.connect("tcp://localhost:%s" % port1)



# Subscribe to zipcode, default is NYC, 10001
# topicfilter = "10001"
# socket.setsockopt_string(zmq.SUBSCRIBE, topicfilter)

# Process 5 updates
total_value = 0
while True:
    message1 = socket.recv()
    message1 = message1.decode("utf-8")
    message1 = json.loads(message1)
    if message1 == "-":
        print("SILENCE")
    else:
        print("pick!")
    print("Done!")

# print("Average messagedata value for topic '%s' was %dF" % (topicfilter, total_value / update_nbr))
      
