# Pydantic Validation file
from pydantic import BaseModel
from typing import List, Optional

#Defines one chat message. Defines one chat message.
class Message(BaseModel):
    role: str
    content: str

# Defines the structure of the request body for POST /chat.
class ChatRequest(BaseModel):
    prompt: str
    history: Optional[List[Message]] = None 
    mode: Optional[str] = "detailed"

'''
Optional[...] = user may send it or may skip it
List[Message] = it should be a list of Message objects
= None = default is no history
Optional response style -> If not provided, default is: detailed
'''

# Defines the structure of the API response.
class ChatResponse(BaseModel):
    response: str       # Defines the structure of the API response.
    model: str          # The model used to generate the answer.