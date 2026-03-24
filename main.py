from fastapi import FastAPI, HTTPException
from config import MODEL
from models import ChatRequest, ChatResponse
from memory import build_messages
from llm import get_ai_response

# Creates the FastAPI application
app = FastAPI(title="AI Chatbot Backend")

@app.get("/")
def root():
    return {"message": "FastAPI AI backend is running"}

@app.post("/chat", response_model=ChatResponse)     # response_model=ChatResponse -> Tells FastAPI that the response should match the ChatResponse schema.
def chat(request: ChatRequest):
    try:                                            # Calls build_messages() to create the final message list.
        messages = build_messages(
            prompt=request.prompt,                  # Passes the new user prompt.
            history=request.history,                # Passes old conversation history if available.
            mode=request.mode                       # Passes response style (short or detailed).
        )

        ai_reply = get_ai_response(messages)        # Sends the built message list to OpenAI and gets the reply.

        return ChatResponse(                        # Creates a structured response object.
            response=ai_reply,                      # Sets the AI text reply.
            model=MODEL
        )                                           # FastAPI converts Chatresponse into JSON automatically.

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))