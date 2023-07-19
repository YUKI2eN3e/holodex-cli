import argparse
from dataclasses import dataclass
from importlib import metadata
from os import path

from rich_argparse import RichHelpFormatter


@dataclass
class CliArgs:
    group: str
    resolution: str


def get_args() -> CliArgs:
    module_name = path.basename(path.dirname(__file__))
    prog_name = module_name.split("_")[0]
    default_group = "Hololive"
    default_resolution = "720"
    parser = argparse.ArgumentParser(prog=prog_name, formatter_class=RichHelpFormatter)
    parser.add_argument(
        "-g",
        "--group",
        help=f"the VTuber group you want to watch (default: {default_group})",
        default=default_group,
    )
    parser.add_argument(
        "-r",
        "--resolution",
        default=default_resolution,
        help=f"the video resolution to play (default: {default_resolution})",
    )
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=f"{prog_name} v{metadata.version(module_name)}",
    )
    return CliArgs(**vars(parser.parse_args()))
