# GeminiAPIChat

## Requirement

To Install dependencies it requires
- [Python](https://www.python.org/downloads/)

This project requires that you have access to an API key.
- [Google Api](https://ai.google.dev/)

## Dependencies

```
pip install python-dotenv
```

Gemini API
```
pip install -q -U google-genai
```

FastAPI
```
pip install fastapi uvicorn python-dotenv
```

Run FastAPI
```
python -m uvicorn ai:app --reload
```
## Setup

Create a file named secret.env containting your API Key.

> **IMPORTANT:** Make sure the variable has the same name as the below example.

Example

```
API_KEY=Your_API_Key
```
