from fastapi import FastAPI
from loguru import logger
from google.genai import types

from config import client,SYSTEM_PROMPT
from schemas import AiRequest


app = FastAPI()

@app.post("/chat")
async def chat_ai(request : AiRequest):
    # llamo a la API haciendo uso de un modelo en particular, y pasandole el prompt
    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=request.question, config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT,
            # max_output_tokens=3,
            temperature=0.5,
        ),
    )
    return {"response": response.text}

