import requests
import streamlink
import subprocess as sp
import holodex.net.apikey as apikey

"""
import os
x_apikey = ""
root_dir = '\\'.join(os.path.abspath(os.path.curdir).split('\\')[0:-1])
with open(f"{root_dir}\\.apikey", "r", encoding="utf8") as file:
    x_apikey = file.readline() 
"""

def check_streams(org):
    api = "https://holodex.net/api/v2/live?org={}".format(org)
    streams_json = requests.get(api, headers={"X-APIKEY": apikey.X_APIKEY})
    live = []
    upcoming = []
    for stream in streams_json.json():
        if stream["status"] == "live":
            live.append(stream)
        else:
            upcoming.append(stream)
    return {"live": live, "upcoming": upcoming}


def open_stream(url, resolution="720p"):
    resolutions = streamlink.streams(url)
    if resolution in resolutions.keys():
        sp.run(["ffplay", resolutions[resolution].url, "-fs"], capture_output=True)
    else:
        sp.run(["ffplay", resolutions["best"].url, "-fs"], capture_output=True)
