from rich.panel import Panel
from textual.app import App, CSSPathType, ComposeResult
from textual.reactive import Reactive
from textual.widget import Widget
from textual.events import Click
from rich.console import RenderableType
from .. import net
from typing import Type
from textual.driver import Driver
from ..util import time
from textual.containers import ScrollableContainer, Container
from textual.binding import Binding
from textual.widgets import Header, Footer

class Stream(Widget):
    def __init__(self, stream_info, name: str = None) -> None:
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

        super().__init__(name=self.title)

    def render(self) -> Panel:
        renderable: RenderableType = "[b]Title:[/b]\t{}\n[b]Member:[/b]\t{}\n[b]Topic:[/b]\t{}\n[b]Status:[/b]\t{}".format(
            self.title, self.member, self.topic, self.status
        )
        return Panel(renderable)

    def on_click(self, event: Click) -> None:
        net.open_stream(self.url)


class ListStreams(App):
    TITLE = "Holodex"
    BINDINGS = [
        ("d", "toggle_dark", "Toggle dark mode"),
        Binding("ctrl+c,ctrl+q", "app.quit", "Quit", show=True),
    ]
    def __init__(
        self,
        org,
        driver_class: Type[Driver] = None,
        css_path: CSSPathType = "styles.css",
        watch_css: bool = False
    ):
        self.org = org
        super().__init__(driver_class, css_path, watch_css)

    def compose(self) -> ComposeResult:
        holodexResponce = net.check_streams(self.org)
        streams = (
            Stream(stream_info)
            for stream_info in (
                holodexResponce["live"]
                if len(holodexResponce["live"]) > 0
                else holodexResponce["upcoming"]
            )
        )
        yield Container(
            Header(name=self.TITLE),
            ScrollableContainer(*streams),
            Footer()
        )
