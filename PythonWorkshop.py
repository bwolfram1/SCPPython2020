import requests
import json
import pandas as pd

response = requests.post("https://postb.in/1580864352476-1852391040883?hello=world")

print(response.status_code)

#What codes mean:

    #200 - Everything is okay 
    #201 - Successfully created
    #301 - redirected to different endpoint
    #400 - bad request/ passed bad data
    #401 - Not authenticated - need API key
    #403 - forbidden request
    #404 = not found
    #503 - Server not ready

#Types of request:

    #Post - create new resource in a collection
    #Get - only to get info
    #Put - update existing resource
    #Delete - Delete a resource
    #Patch - partial update to resource 

def getJson(uri, params = None):
    response = requests.get(uri, params)
    rjson = response.json()
    return rjson

Djson = getJson("http://api.open-notify.org/astros.json")["people"]
df = pd.DataFrame.from_dict(Djson)

parameters = {
    "lat": 28.0551763,
    "lon": -82.4210919
}

DISSOver = getJson("http://api.open-notify.org/iss-pass.json", params=parameters)["response"]
dfISS = pd.DataFrame.from_dict(DISSOver)

from datetime import datetime

times = []

for rt in dfISS["risetime"]:
    time = datetime.fromtimestamp(rt)
    times.append(time)
    print(time)
dfISS["risetime"] = times




