from rich.panel import Panel
from textual.app import App
from textual.reactive import Reactive
from textual.widget import Widget
from textual.events import Click
from rich.console import RenderableType
from .. import net
from typing import Type
from textual.driver import Driver


class Stream(Widget):
    def __init__(self, stream_info, name: str = None) -> None:
        self.title = stream_info["title"]
        self.member = stream_info["channel"]["english_name"]
        self.topic = stream_info["topic_id"].title().replace("_", " ")
        self.url = "https://youtu.be/{}".format(stream_info["id"])
        self.status = (
            "[b blink red]LIVE[/]" if stream_info["status"] == "live" else "Upcoming"
        )

        super().__init__(self.title)

    def render(self) -> Panel:
        renderable: RenderableType = "[b]Title:[/b]\t{}\n[b]Member:[/b]\t{}\n[b]Topic:[/b]\t{}\n[b]Status:[/b]\t{}".format(
            self.title, self.member, self.topic, self.status
        )
        return Panel(renderable)

    def on_click(self, event: Click) -> None:
        net.open_stream(self.url)


class ListStreams(App):
    def __init__(self, org, screen: bool = True, driver_class: Type[Driver] = None, log: str = "", log_verbosity: int = 1, title: str = "Holodex"):
        self.org = org

        super().__init__(screen, driver_class, log, log_verbosity, title)

    async def on_load(self) -> None:
        """Bind keys here."""
        await self.bind("q", "quit", "Quit")

    async def on_mount(self) -> None:
        streams = (Stream(stream_info) for stream_info in net.check_streams(self.org)["live"])
        await self.view.dock(*streams, edge="top")
