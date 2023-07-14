#!/usr/bin/env python3
import argparse
from dataclasses import dataclass

from holodex.ui import ListStreams


@dataclass
class CliArgs:
    group: str


def get_args() -> CliArgs:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-g", "--group", help="The VTuber group you want to watch", default="Hololive"
    )
    return CliArgs(**vars(parser.parse_args()))


def run():
    args = get_args()
    group = str(args.group)
    if (
        group.title() == "Hololive"
        or group.title() == "Nijisanji"
        or group.title() == "Independents"
    ):
        group = group.title()
    elif group.title() == "Niji":
        group = "Nijisanji"
    elif group.upper() == "VOMS":
        group = group.upper()
    elif group.title() == "Indie":
        group = "Independents"

    app = ListStreams(org=group)
    app.run()


if __name__ == "__main__":
    run()
