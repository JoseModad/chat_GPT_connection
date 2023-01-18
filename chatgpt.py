import openai

from dotenv import load_dotenv

import os

load_dotenv()

KEY_OPENAPI = os.getenv("KEY_OPENAPI")

openai.api_key = f"{KEY_OPENAPI}"

prompt = input("Ingrese el tema en el que te puedo ayudar? ")

response = openai.Completion.create(
    engine = "text-davinci-003",
    prompt = prompt,
    max_tokens = 1024,
    
)

print(response["choices"][0]["text"])