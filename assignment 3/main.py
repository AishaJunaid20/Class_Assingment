# main.py

import chainlit as cl
from country_info_toolkit import get_country_info

@cl.on_message
async def main(message: cl.Message):
    response = get_country_info(message.content)
    await cl.Message(content=response).send()
