#!/usr/bin/env python3
from .ui import ListStreams
import argparse

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-g', '--group', help="The VTuber group you want to watch", default="Hololive")
    return parser.parse_args()

def run():
    args = get_args()
    group = args.group
    if args.group.title() == "Hololive" or args.group.title() == "Nijisanji" or args.group.title() == "Independents":
        group =  args.group.title()
    elif args.group.upper() == "VOMS":
        group = args.group.upper()
    elif args.group.title() == "Indie":
        group = "Independents"
    

    ListStreams.run(org=group)


if __name__ == "__main__":
    run()
