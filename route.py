#!/usr/bin/python

import requests
import yaml

URL = "https://maps.googleapis.com/maps/api/directions/json"
CONFIG_FILE = "config.yml"

def makeRequest():
    parameters = {
        "departure_time": "now",
        "alternatives": "true",
        "avoid": "tolls"
    }
    with open(CONFIG_FILE, "r") as s:
        try:
            y = yaml.safe_load(s)
            parameters["origin"] = y['Origin'].replace(" ", "+"),
            parameters["destination"] = y['Dest'].replace(" ", "+"),
            parameters["key"] = y['Google_Maps_API_Key']
        except yaml.YAMLError as exc:
            print exc
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
