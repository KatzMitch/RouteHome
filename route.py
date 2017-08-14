#!/usr/bin/python

import requests
import yaml

URL = "https://maps.googleapis.com/maps/api/directions/json"
API_KEY_FILE = "apikey.yml"

ORIGIN = "311 Arsenal St, Watertown, MA"
DEST = "137 W Concord St, Boston, MA"

def getAPIKey():
    with open(API_KEY_FILE, "r") as s:
        try:
            y = yaml.safe_load(s)
            return y["Google_Maps_API_Key"]
        except yaml.YAMLError as exc:
            print exc

def makeRequest(org=ORIGIN, dest=DEST):
    parameters = {
        "origin": org.replace(" ", "+"),
        "destination": dest.replace(" ", "+"),
        "key": getAPIKey(),
        "departure_time": "now",
        "alternatives": "true",
        "avoid": "tolls"
    }
    req = requests.get(URL, params=parameters)
    return req.json()

def printResponse(r):
    if r["status"] != "OK":
        raise r["error_message"]
    print("There are " + str(len(r['routes'])) + " routes home")
    for route in r['routes']:
        print (route["summary"] + " will take "
                    + route['legs'][0]['duration_in_traffic']['text'])

if __name__ == "__main__":
    r = makeRequest()
    printResponse(r)