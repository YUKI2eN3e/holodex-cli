import requests
import streamlink
import subprocess as sp

streams_json = requests.get("https://holodex.net/api/v2/live?org=Hololive")
live = []
live_i = 0
upcoming = []
for stream in streams_json.json():
    if stream["status"] == "live":
        live.append(stream)
    else:
        upcoming.append(stream)


def open_stream(url, resolution="720p"):
    resolutions = streamlink.streams(url)
    if resolution in resolutions.keys():
        sp.run(
            ["mpv", resolutions[resolution].url], capture_output=True
        )
    else:
        sp.run(["mpv", resolutions["best"].url], capture_output=True)
