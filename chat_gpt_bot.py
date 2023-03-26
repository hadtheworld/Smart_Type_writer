#!/usr/bin/env python3
#Import open AI OS and System Modules
import openai
openai.api_key = "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"

def chat(inp):
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": "You are a chatbot"},
            {"role": "user", "content": inp},
        ]
        )
    result = ''
    for choice in response.choices:
        result += choice.message.content
    return result
print(chat("who are you?"))
