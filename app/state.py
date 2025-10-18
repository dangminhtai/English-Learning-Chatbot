import reflex as rx
import asyncio
from typing import TypedDict


class Message(TypedDict):
    """A chat message."""

    role: str
    content: str


class ChatState(rx.State):
    """The state for the chat application."""

    messages: list[Message] = [
        {
            "role": "assistant",
            "content": "Hello! I'm your English learning assistant. What would you like to practice today?",
        },
        {
            "role": "user",
            "content": "Hi there! I'd like to practice ordering food at a restaurant.",
        },
        {
            "role": "assistant",
            "content": "Excellent choice! Let's begin. I'll be the waiter. 'Good evening, welcome to The Reflex Bistro. Do you have a reservation?'",
        },
    ]
    current_message: str = ""
    is_processing: bool = False

    @rx.event
    def on_message_change(self, value: str):
        """Handle changes in the message input field."""
        self.current_message = value

    @rx.event
    async def send_message(self):
        """Send the user's message and get a response."""
        if not self.current_message.strip():
            return
        user_message = {"role": "user", "content": self.current_message}
        self.messages.append(user_message)
        self.current_message = ""
        yield
        self.is_processing = True
        yield
        await asyncio.sleep(1.5)
        ai_response = {
            "role": "assistant",
            "content": f"That's an interesting topic! You said: '{user_message['content']}'. Let's talk more about that.",
        }
        self.messages.append(ai_response)
        self.is_processing = False
        yield