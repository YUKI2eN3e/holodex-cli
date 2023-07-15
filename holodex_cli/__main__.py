#!/usr/bin/env python3
from holodex_cli import cli
from holodex_cli.ui import ListStreams


def run():
    args = cli.get_args()
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

    app = ListStreams(org=group, resolution=args.resolution)
    app.run()


if __name__ == "__main__":
    run()
