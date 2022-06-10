
# Copyright 2020 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import logging
import random
from tabnanny import check
from flask import Flask, request
import json

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
logger = logging.getLogger(__name__)

app = Flask(__name__)
moves = ['F', 'T', 'L', 'R']
onlyMoves =['F','L','R']
myapp="https://jack-cloud-run-hackathon-python-audhxybk5q-uc.a.run.app"
FORWARD="FORWARD"
THROW="THROW"
LEFT="LEFT"
RIGHT="RIGHT"
tototalUser=[]

myCurrentState = ''

@app.route("/", methods=['GET'])
def index():
    return "Let the battle begin!"

@app.route("/", methods=['POST'])
def move():
    request.get_data()
    logger.info(request.json)
    print("================")

    objectString=json.dumps(request.json)
    object = json.loads(objectString)

    
    
    
    totalState=object["arena"]["state"]

    for user in totalState:
        if '.run.app' in user :
            print(user)
            tototalUser.append(user)

    print("userarr= " + str(tototalUser))


    myCurrentState = totalState[myapp]

    print("mycruuecnt " + str(myCurrentState))
    print("user === " + str(totalState[tototalUser[1]]))
    print("myDir = " + checkMyDir(myCurrentState))
    print("path" + str(checkActtackPath(myCurrentState)))



    
    if checkMyDir(myCurrentState) == "N":
        for userState in tototalUser:
            if totalState[userState]["x"] == myCurrentState["x"]:
                for path in checkActtackPath(myCurrentState):
                    if path == totalState[userState]["y"]:
                        print("✅✅✅✅✅attack NNN✅✅✅✅✅")
                        return moveAction(THROW)
    elif checkMyDir(myCurrentState) == "E":
        for userState in tototalUser:
            if totalState[userState]["y"] == myCurrentState["y"]:
                for path in checkActtackPath(myCurrentState):
                    if path == totalState[userState]["x"]:
                        print("✅✅✅✅✅attack EEE✅✅✅✅✅")
                        return moveAction(THROW)
    elif checkMyDir(myCurrentState) == "S": 
        for userState in tototalUser:
            if totalState[userState]["x"] == myCurrentState["x"]:
                for path in checkActtackPath(myCurrentState):
                    if path == totalState[userState]["y"]:
                        print("✅✅✅✅✅attack SSS✅✅✅✅✅")
                        return moveAction(THROW)
    elif checkMyDir(myCurrentState) == "W":
        for userState in tototalUser:
            if totalState[userState]["y"] == myCurrentState["y"]:
                for path in checkActtackPath(myCurrentState):
                    if path == totalState[userState]["y"]:
                        print("✅✅✅✅✅attack WWW✅✅✅✅✅")
                        return moveAction(THROW)
    elif myCurrentState["wasHit"]:
        return moveAction(FORWARD)    
    return moves[random.randrange(len(moves))]
 

    # return modifyPosition(myCurrentState)


def checkEnemy(enemyState):
    x=enemyState["x"]
    y=enemyState["y"]
    

def checkMyDir(myState):
    direction=myState["direction"]
    return direction

def checkActtackPath(myState):
    x=myState["x"]
    y=myState["y"]
    direction=myState["direction"]
    if direction == "N":
        return [y-1,y-2,y-3]
    elif direction == "E":
        return [x+1,x+2,x+3]
    elif direction == "S":
        return [y+1,y+2,y+3]
    elif direction == "W":
        return [x-1,x-2,x-3]



def modifyPosition(myState):
    x=myState["x"]
    y=myState["y"]
    direction=myState["direction"]
    wasHit=myState["wasHit"]
    score=myState["score"]
    myInfo="My Detail Info: \nX= " + str(x) + "  \nY= " + str(y) + " \ndirection = " + direction + " \nwasHit = " + str(wasHit) + " \nscroe = " + str(score) 
    print("✅✅✅✅✅ \n" + myInfo + "\n✅✅✅✅✅")




    
    



def moveAction(status):
    if status == FORWARD:
        return moves[0]
    elif status == THROW:
        return moves[1]
    elif status == LEFT:
        return moves[2]
    elif status == RIGHT:
        return moves[3]
    else:
        return "ERROR"


if __name__ == "__main__":
  app.run(debug=False,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
  
