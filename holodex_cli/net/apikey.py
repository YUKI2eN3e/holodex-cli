from sys import version

if (
    float(
        version.split(" ")[0].removesuffix(f".{version.split(' ')[0].split('.')[-1]}")
    )
    < 3.11
):
    import tomli as toml
else:
    import tomllib as toml

import os

SEP = os.path.sep


def get_user_config_path() -> str:
    return f"{os.path.expanduser('~')}{SEP}.local{SEP}holodex-cli{SEP}config.toml"


try:
    with open(get_user_config_path(), "rb") as file:
        config = toml.load(file)
    X_APIKEY = config["API_KEY"]
except Exception:
    from rich.console import Console

    console = Console()
    console.print_exception(show_locals=True)
    console.print(
        f"[red bold]No config.toml/API_KEY found.\nPlease make sure {get_user_config_path()} contains your Holodex.net API_KEY stored as instructed in README.md[/red bold]"
    )
    exit()
