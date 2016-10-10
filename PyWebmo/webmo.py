from websocket import create_connection
import json

class Webmo:
    def __init__(self,address):
        self.wsInst = create_connection(address)

    def rotate(self,speed):
        sObj = {
            "type" : "rotate",
            "speed" : speed
        }
        self.wsInst.send(json.dumps(sObj))

    def rotateTo(self,degree,absRange,speed):
        sObj = {
            "type" : "rotateTo",
            "target" : degree,
            "absRange" : absRange,
            "speed" : speed
        }
        self.wsInst.send(json.dumps(sObj))

    def rotateBy(self,diff,speed):
        sObj = {
            "type" : "rotateBy",
            "diff" : diff,
            "speed" : speed
        }
        self.wsInst.send(json.dumps(sObj))

    def stop(self,smooth = False,lock = False):
        sObj = {
            "type" : "stop",
            "smooth" : smooth,
            "lock" : lock
        }
        self.wsInst.send(json.dumps(sObj))

    def stopHard(self):
        self.stop(false)

    def stopSoft(self):
        self.stop(true)
