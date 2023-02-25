#!/usr/bin/env python3
from .ui import ListStreams
import argparse

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-g', '--group', help="The VTuber group you want to watch", default="Hololive")
    return parser.parse_args()

def run():
    args = get_args()
    group = str(args.group)
    if group.title() == "Hololive" or group.title() == "Nijisanji" or group.title() == "Independents":
        group =  group.title()
    elif group.title() == "Niji":
        group = "Nijisanji"
    elif group.upper() == "VOMS":
        group = group.upper()
    elif group.title() == "Indie":
        group = "Independents"
    
    ListStreams.run(org=group)


if __name__ == "__main__":
    run()
