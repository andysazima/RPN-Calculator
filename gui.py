from textual.containers import Container
from textual.widgets import Button, Static
from textual.app import App, ComposeResult


class CalculatorApp(App):

    def compose(self) -> ComposeResult:
        yield Static("One", classes="box")
        yield Static("Two", classes="box")
