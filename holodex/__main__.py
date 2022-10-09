#!/usr/bin/env python3
from .ui import ListStreams
import argparse

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-g', '--group', help="The VTuber group you want to watch", default="Hololive")
    return parser.parse_args()

def run():
    args = get_args()
    ListStreams.run(org=args.group)


if __name__ == "__main__":
    run()
