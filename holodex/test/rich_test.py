#!/usr/bin/env python3
from rich.panel import Panel
from textual.app import App
from textual.reactive import Reactive
from textual.widget import Widget
from textual.events import Click


class Clicker(Widget):

    clicked = Reactive(False)

    def render(self) -> Panel:
        return Panel("Hello [b]World[/b]", style=("on red" if self.clicked else ""))

    def on_click(self, event: Click) -> None:
        self.clicked = not self.clicked


class ClickApp(App):
    """Demonstrates custom widgets"""

    async def on_mount(self) -> None:
        clicks = (Clicker() for _ in range(10))
        await self.view.dock(*clicks, edge="top")


if __name__ == "__main__":
    ClickApp.run()
