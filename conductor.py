'''
This program is supposed to provide the beat and
notes for the pitch and string processes

'''


import zmq
import random
import sys
import time
import json


def decoder(note_string):

    decoded = [*note_string]

    music_length = len(decoded)



    return music_length, decoded


message = []

RAW_NOTES = "----EEFGGFEDCCDEE-D-EEFGGFEDCCDED-C-"

metronome = 100


music_length, decoded = decoder(RAW_NOTES)








port = "5556"
if len(sys.argv) > 1:
    port =  sys.argv[1]
    int(port)

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:%s" % port)

for i in range(music_length):
    msg = decoded[i]
    # print("%d %d" % (topic, messagedata))
    # socket.send_string(json.dumps("%d %d" % (topic, messagedata)))
    socket.send_string(json.dumps(msg))
    print("SENT")
    time.sleep(60/metronome)


