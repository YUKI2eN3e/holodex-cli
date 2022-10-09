from rich.panel import Panel
from textual.app import App
from textual.reactive import Reactive
from textual.widget import Widget
from textual.events import Click
from rich.console import RenderableType
from .. import net


class Stream(Widget):
    def __init__(self, name: str = None) -> None:

        stream_info = net.live[net.live_i]
        net.live_i += 1
        self.title = stream_info["title"]
        self.member = stream_info["channel"]["english_name"]
        self.topic = stream_info["topic_id"].title()
        self.url = "https://youtu.be/{}".format(stream_info["id"])

        super().__init__(name)

    def render(self) -> Panel:
        renderable: RenderableType = (
            "[b]Title:[/b]\t{}\n[b]Member:[/b]\t{}\n[b]Topic:[/b]\t{}".format(
                self.title, self.member, self.topic
            )
        )
        return Panel(renderable, expand=False)

    def on_click(self, event: Click) -> None:
        net.open_stream(self.url)


class ListStreams(App):
    async def on_mount(self) -> None:
        streams = (Stream() for _ in range(len(net.live) - 1))
        await self.view.dock(*streams, edge="top")
