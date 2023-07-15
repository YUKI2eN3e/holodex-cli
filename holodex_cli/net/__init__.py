import subprocess as sp

import requests
import streamlink

from holodex_cli.net.apikey import X_APIKEY


def check_streams(org):
    api = "https://holodex.net/api/v2/live?org={}".format(org)
    streams_json = requests.get(api, headers={"X-APIKEY": X_APIKEY})
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
