#import app.main as main
#main.main_menu()

import configparser
config = configparser.ConfigParser()
config.read('config/app.ini')

from textual.app import App, ComposeResult
from textual.containers import ScrollableContainer, Container
from textual.widgets import Header, Footer, Static, Label, Button, RadioButton, RadioSet

class TitleHeader(Static):
    """A simple introduction widget."""
    def compose(self) -> ComposeResult:
        yield Label("|\/|/\|\/|/\| Trylobyte", id="title", classes="box")
        yield RadioSet("Simple", "Advanced", id="ui-toggle", classes="box")
        yield Label("Status: " + "DEBUG", id="status", classes="box")

class MainMenu(Static):
    """A simple main menu widget."""
    def compose(self) -> ComposeResult:
        yield Container(Label("Main Menu", id="main_menu"))

class TrylobyteApp(App):
    CSS_PATH = "app/css/main.tcss"
    BINDINGS = [
        ("d", "toggle_dark", "Toggle Dark Mode"),
        ("q", "quit", "Quit")
        ]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Container(TitleHeader(expand=True), MainMenu())
        yield Footer()

    def on_mount(self) -> None:
        self.title = "Trylobyte"
        self.sub_title = "Main Menu"

    def action_toggle_dark(self) -> None:
        self.dark = not self.dark
    def action_quit(self) -> None:
        self.exit()

if __name__ == "__main__":
    app = TrylobyteApp()
    app.run()
