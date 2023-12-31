"""The main Chat app."""

import reflex as rx

from webui import styles
from webui.components import chat, modal, navbar, sidebar
from webui.state import State


def index() -> rx.Component:
    """The main app."""
    return rx.vstack(
        navbar(),
        chat.chat(),
        chat.action_bar(),
        sidebar(),
        modal(),
        bg=styles.bg_dark_color,
        color=styles.text_light_color,
        min_h="100vh",
        align_items="stretch",
        spacing="0",
    )
def kg()-> rx.Component:
    return rx.html("<iframe src='/graph.html' style='width:100vw; height:100vh;' frameborder='0'></iframe>")
app = rx.App(state=State, style=styles.base_style)
app.add_page(index)
app.add_page(kg, "/kg")
app.compile()
