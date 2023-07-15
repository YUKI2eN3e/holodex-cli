from typing import Type

from rich.console import RenderableType
from rich.panel import Panel
from textual.app import App, ComposeResult, CSSPathType
from textual.binding import Binding
from textual.containers import Container, ScrollableContainer
from textual.driver import Driver
from textual.events import Click
from textual.reactive import Reactive
from textual.widget import Widget
from textual.widgets import Footer, Header

from holodex_cli import net
from holodex_cli.util import time


class Stream(Widget):
    def __init__(self, stream_info, resolution: str, name: str = None) -> None:
        self.title = stream_info["title"]
        self.member = stream_info["channel"]["english_name"]
        self.topic = str()
        try:
            self.topic = stream_info["topic_id"].title().replace("_", " ")
        except KeyError:
            self.topic = "Chat"
        self.url = "https://youtu.be/{}".format(stream_info["id"])
        self.status = (
            "[b blink red]LIVE[/]"
            if stream_info["status"] == "live"
            else "Upcoming in: {}".format(
                str(time.time_until(stream_info["start_scheduled"])).split(".")[0]
            )
        )
        self.resolution = resolution if resolution[-1] == "p" else resolution + "p"

        super().__init__(name=self.title)

    def render(self) -> Panel:
        renderable: RenderableType = "[b]Title:[/b]\t{}\n[b]Member:[/b]\t{}\n[b]Topic:[/b]\t{}\n[b]Status:[/b]\t{}".format(
            self.title, self.member, self.topic, self.status
        )
        return Panel(renderable)

    def on_click(self, event: Click) -> None:
        net.open_stream(url=self.url, resolution=self.resolution)


class ListStreams(App):
    TITLE = "Holodex"
    BINDINGS = [
        ("d", "toggle_dark", "Toggle dark mode"),
        Binding("q,ctrl+c", "app.quit", "Quit", show=True, key_display="Q"),
    ]

    def __init__(
        self,
        org: str,
        resolution: str,
        driver_class: Type[Driver] = None,
        css_path: CSSPathType = "styles.css",
        watch_css: bool = False,
    ):
        self.org = org
        self.resolution = resolution
        super().__init__(driver_class, css_path, watch_css)

    def compose(self) -> ComposeResult:
        holodex_response = net.check_streams(self.org)
        streams = (
            Stream(stream_info, self.resolution)
            for stream_info in (
                holodex_response["live"] + holodex_response["upcoming"]
                if len(holodex_response["live"]) > 0
                else holodex_response["upcoming"]
            )
        )
        yield Container(
            Header(name=self.TITLE), ScrollableContainer(*streams), Footer()
        )
