import reflex as rx
from app.state import ChatState
from app.components import chat_header, message_bubble, message_input, typing_indicator


def index() -> rx.Component:
    """The main chat interface."""
    return rx.el.main(
        rx.el.div(
            chat_header(),
            rx.el.div(
                rx.el.div(
                    rx.foreach(ChatState.messages, message_bubble),
                    rx.cond(ChatState.is_processing, typing_indicator(), rx.fragment()),
                    class_name="flex flex-col gap-6 p-4 md:p-6",
                ),
                class_name="flex-grow overflow-y-auto",
            ),
            message_input(),
            class_name="flex flex-col h-screen bg-gray-50",
        ),
        class_name="font-['Inter']",
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(index, title="LingoBuddy")