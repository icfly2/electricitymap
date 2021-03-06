#!/usr/bin/python

import requests

#Parser for South Australia's 129MWh battery built by Tesla.
#base_url gets generation status in 5 min intervals.

base_url = 'https://ausrealtimefueltype.global-roam.com/api/SeriesSnapshot?time='

def fetch_SA_battery():
    """
    Makes a request to the NemWatch widget data source.
    Finds dictionaries related to the South Australia battery.
    Returns a float.
    """

    #Verify set to false to prevent SSL error due to domain mismatch.
    req = requests.get(base_url, verify = False)
    json_content = req.json()
    dicts = json_content["seriesCollection"]
    discharge_id = (item for item in dicts if item["id"] == "41").next()
    storage_id = (item for item in dicts if item["id"] == "57").next()

    discharge = -1*float(discharge_id["value"])
    storage = float(storage_id["value"])

    #one of these should always be zero
    battery_status = discharge + storage

    return battery_status


if __name__ == '__main__':
    print('fetch_SA_battery() ->')
    print(fetch_SA_battery())
