# FastAPI AI Backend (LLM Chatbot)

A production-style AI backend built using **FastAPI** and **OpenAI API** that supports conversational chat with memory and structured responses.

---

## Live Demo

 https://fastapi-ai-backend.onrender.com/docs

---

## Features

* 🔹 FastAPI-based REST API
* 🔹 OpenAI LLM integration (`gpt-4o-mini`)
* 🔹 Conversation memory support
* 🔹 Structured responses (short / detailed mode)
* 🔹 Clean modular architecture
* 🔹 Swagger UI for testing
* 🔹 Environment-based configuration (.env)

---

## Project Structure

```text
fastapi-ai-backend/
│── main.py          # FastAPI app (routes)
│── llm.py           # OpenAI API interaction
│── memory.py        # Builds conversation messages
│── models.py        # Request/response schemas
│── config.py        # Loads environment variables
│── requirements.txt # Dependencies
│── .python-version  # Python version for deployment
│── .gitignore
│── README.md
```

---

## Tech Stack

* FastAPI
* OpenAI API
* Pydantic
* Uvicorn
* Python 3.11

---

## API Flow

```text
User → FastAPI → Pydantic → Memory Builder → OpenAI → Response → User
```

---

## Installation (Local Setup)

### 1. Clone repository

```bash
git clone https://github.com/pawarsamradnyee/fastapi-ai-backend.git
cd fastapi-ai-backend
```

---

### 2. Create virtual environment

```bash
python -m venv venv
```

Activate:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Create `.env` file

```env
OPENAI_API_KEY=your_api_key_here
```

---

### 5. Run server

```bash
uvicorn main:app --reload
```

---

### 6. Open Swagger UI

```text
http://127.0.0.1:8000/docs
```

---

## API Usage

### POST `/chat`

#### Request Body

```json
{
  "prompt": "What is FastAPI?",
  "history": [],
  "mode": "detailed"
}
```

---

#### Response

```json
{
  "response": "FastAPI is a modern Python framework...",
  "model": "gpt-4o-mini"
}
```

---

## Key Components

| File        | Purpose            |
| ----------- | ------------------ |
| `main.py`   | API endpoints      |
| `models.py` | Data validation    |
| `memory.py` | Context building   |
| `llm.py`    | OpenAI integration |
| `config.py` | Environment setup  |

---

## Environment Variables

| Variable       | Description                       |
| -------------- | --------------------------------- |
| OPENAI_API_KEY | Your OpenAI API key               |
| MODEL          | Model name (default: gpt-4o-mini) |

---

## Deployment (Render)

1. Push code to GitHub
2. Create Web Service on Render
3. Use:

```bash
Build: pip install -r requirements.txt
Start: uvicorn main:app --host 0.0.0.0 --port $PORT
```

4. Add environment variables in Render dashboard

---

## Summary

> Built a FastAPI-based AI backend integrated with OpenAI. The system validates input using Pydantic, constructs conversational context, sends it to the LLM, and returns structured responses. Deployed on Render using environment variables for secure configuration.

---

## Future Improvements

* Add database (chat history persistence)
* Streaming responses
* Authentication (JWT)
* Frontend UI (React)
* RAG (Retrieval-Augmented Generation)

---

## Author

**Samradnyee**

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
