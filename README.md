# SOEN472-MiniProject

Intelligent Support Assistant with Sentiment Analysis and Retrieval
— COMP 472 (Artificial Intelligence), Summer 2026, Mini Project 1.

An AI-powered student support assistant that answers questions from a knowledge
base, detects user sentiment, recommends escalation for frustrated students,
and retrieves the most relevant answer using semantic similarity.

## Project structure

| File | Purpose |
|------|---------|
| `main.py` | Entry point — interactive conversation loop |
| `assistant.py` | `SupportAssistant` class (KB loading, embeddings, search, sentiment, escalation) |
| `knowledge_base.csv` | Questions and answers (`question,answer` format) |
| `requirements.txt` | Python dependencies |
| `reflection.md` | Team reflection (deliverable) |

## Setup

```bash
pip install -r requirements.txt
```

## Run

```bash
python main.py
```

Type `quit` to exit.

> Status: skeleton / frame — AI components are stubbed and need to be implemented.
