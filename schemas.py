from pydantic import BaseModel

class AiRequest(BaseModel):
    question: str
