# Evidence Answering Bot for Clinicians - Track 3

This project implements **Track 3 - Evidence Answering for Clinicians** from HackWithChicago 2.0.

It provides a clinician facing Q and A API that retrieves answers from a live corpus of guidelines
and research papers, using Pathway as the streaming document store and live index.

## What it does

- Ingests guideline and trial snippets as a simulated live document stream
- Keeps an always up to date Pathway table of evidence documents
- Answers clinical questions with concise responses and numbered citations
- Returns quoted text from each cited source
- Demonstrates that adding a new paper changes future answers

## Tech stack

- Pathway for streaming ingestion and indexing
- Pathway LLM xPack for RAG style answering (hook location in code)
- FastAPI HTTP service
- Optional web scraping connector via Pathway in `pathway_pipeline.py`

## Demo story

1. Ingest a few fake guideline documents with `/evidence/ingest`.
2. Ask a question through `/evidence/ask`.
3. Show the answer and its citations.
4. Ingest a new synthetic paper that mentions a different recommendation.
5. Ask a follow up question and call out how the answer now references the new source.

This is a decision support demo only and does not give medical advice.
