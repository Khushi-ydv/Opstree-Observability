# Agent Observability Demo

Simple LangGraph agent (Gemini + a mock weather tool), traced to LangSmith.

## Setup

1. Copy `.env.example` to `.env` and fill in your keys.
2. `python3 -m venv .venv`
3. `.venv/bin/pip install -r requirements.txt`

## Run the UI

```
.venv/bin/streamlit run app.py
```

Enter a query in the text box and click "Run agent".

## Run in terminal

Case 1 — success (clean run, correct output):

```
.venv/bin/python agent.py
```

Case 2 — failure (tool raises an exception, visible as a failed trace in LangSmith):

```
.venv/bin/python agent.py --break
```

All runs appear in your LangSmith project (`LANGCHAIN_PROJECT` in `.env`).
