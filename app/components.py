import reflex as rx
from app.state import ChatState


def message_bubble(message: dict) -> rx.Component:
    """Creates a chat bubble for a message."""
    is_user = message["role"] == "user"
    base_style = "p-3 md:p-4 max-w-lg"
    return rx.el.div(
        rx.el.div(
            rx.el.p(message["content"], class_name="text-sm md:text-base font-medium"),
            class_name=rx.cond(
                is_user,
                f"{base_style} bg-emerald-600 text-white rounded-t-2xl rounded-l-2xl",
                f"{base_style} bg-gray-200 text-gray-800 rounded-t-2xl rounded-r-2xl",
            ),
            style={"box_shadow": "0px 1px 3px rgba(0,0,0,0.12)"},
        ),
        class_name=rx.cond(
            is_user, "w-full flex justify-end", "w-full flex justify-start"
        ),
    )


def chat_header() -> rx.Component:
    """The header for the chat application."""
    return rx.el.header(
        rx.el.div(
            rx.el.div(
                rx.icon("message-circle-more", class_name="w-6 h-6 text-emerald-600"),
                rx.el.h1(
                    "LingoBuddy",
                    class_name="text-xl md:text-2xl font-bold text-gray-800 tracking-tight",
                ),
                class_name="flex items-center gap-3",
            ),
            rx.el.div(
                rx.el.button(
                    rx.icon("settings", class_name="w-5 h-5"),
                    class_name="p-2 rounded-full text-gray-600 hover:bg-gray-200 hover:text-gray-800 transition-colors",
                ),
                rx.el.button(
                    rx.icon("user", class_name="w-5 h-5"),
                    class_name="p-2 rounded-full text-gray-600 hover:bg-gray-200 hover:text-gray-800 transition-colors",
                ),
                class_name="flex items-center gap-2",
            ),
            class_name="flex items-center justify-between w-full max-w-5xl mx-auto px-4",
        ),
        style={"box_shadow": "0px 4px 8px rgba(0,0,0,0.08)"},
        class_name="w-full h-16 bg-white/80 backdrop-blur-sm sticky top-0 z-10 flex items-center border-b border-gray-200",
    )


def message_input() -> rx.Component:
    """The message input field and send button."""
    return rx.el.div(
        rx.el.div(
            rx.el.input(
                placeholder="Practice your English...",
                on_change=ChatState.on_message_change,
                class_name="flex-grow bg-transparent focus:outline-none text-gray-800 placeholder-gray-500 text-base font-medium",
                default_value=ChatState.current_message,
            ),
            rx.el.button(
                rx.icon("send", class_name="w-6 h-6"),
                on_click=ChatState.send_message,
                disabled=ChatState.is_processing
                | (ChatState.current_message.strip() == ""),
                class_name="bg-emerald-600 text-white p-3 rounded-full hover:bg-emerald-700 transition-all duration-300 disabled:bg-gray-300 disabled:cursor-not-allowed",
                style={
                    "box_shadow": rx.cond(
                        ChatState.is_processing
                        | (ChatState.current_message.strip() == ""),
                        "none",
                        "0px 4px 8px rgba(0,0,0,0.15)",
                    )
                },
            ),
            class_name="flex items-center gap-4 w-full max-w-4xl mx-auto p-2 pl-6 bg-white rounded-full",
            style={"box_shadow": "0px 4px 12px rgba(0,0,0,0.1)"},
        ),
        class_name="w-full p-4 sticky bottom-0 z-10 bg-gradient-to-t from-gray-100 to-transparent",
    )


def typing_indicator() -> rx.Component:
    """A typing indicator to show when the assistant is 'typing'."""
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    class_name="w-2 h-2 bg-gray-400 rounded-full animate-bounce [animation-delay:-0.3s]"
                ),
                rx.el.div(
                    class_name="w-2 h-2 bg-gray-400 rounded-full animate-bounce [animation-delay:-0.15s]"
                ),
                rx.el.div(class_name="w-2 h-2 bg-gray-400 rounded-full animate-bounce"),
                class_name="flex items-center gap-2",
            ),
            class_name="bg-gray-200 text-gray-800 rounded-t-2xl rounded-r-2xl p-4 max-w-lg",
            style={"box_shadow": "0px 1px 3px rgba(0,0,0,0.12)"},
        ),
        class_name="w-full flex justify-start",
    )