import zmq
import zlib
import json
import graphics

context = zmq.Context()

#  Socket to talk to server
print("Connecting to eddn server...")
socket = context.socket(zmq.SUB)
socket.connect("tcp://eddn.edcd.io:9500")

print("Subscribing...")
socket.setsockopt(zmq.SUBSCRIBE, b"")

win = graphics.GraphWin(width=1000, height=1000)
win.setCoords(-45000, -20000, 45000, 70000)
img = graphics.Image(graphics.Point(0, 25000), "Galaxy_L_Grid.ppm")
img.draw(win)

print("Waiting for events...")
while True:
    #  Get a reply.
    message = socket.recv()
    j = json.loads(zlib.decompress(message))
#    schema = j["$schemaRef"].split("/")[-2]
#    print("----------------------------")
#    print(schema)
#    print(json.dumps(j["message"]))
    if "StarPos" in j["message"]:
        pos = j["message"]["StarPos"]
        p = graphics.Point(pos[0], pos[2])
        p.setFill("yellow")
        p.draw(win)

    win.checkMouse()
