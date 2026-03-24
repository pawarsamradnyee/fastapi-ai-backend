# API communication file
from openai import OpenAI
from config import OPENAI_API_KEY, MODEL

client = OpenAI(api_key=OPENAI_API_KEY)                     # Creates the API client using your API key.

# a function that sends messages to the model and gets an answer.
def get_ai_response(messages):
    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,                                  # Sends the conversation list to the model. This contains system prompt, history, and latest user prompt.
        temperature=0.7
    )
    return response.choices[0].message.content.strip() 

'''
response.choices[0] = first result
.message.content = text of the answer
.strip() = removes extra spaces/newlines from beginning and end
'''