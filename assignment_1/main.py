# main.py

import chainlit as cl
from product_suggester import suggest_product

@cl.on_message
async def handle_message(message: cl.Message):
    user_input = message.content
    response = suggest_product(user_input)
    await cl.Message(content=response).send()
