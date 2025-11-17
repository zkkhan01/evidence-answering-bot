from __future__ import annotations

import uuid
from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List

from .schemas import EvidenceSnippet


@dataclass
class EvidenceDoc:
    id: str
    title: str
    content: str
    source_type: str
    ingested_at: datetime


class EvidenceStore:
    def __init__(self) -> None:
        self._docs: Dict[str, EvidenceDoc] = {}

    def add(self, doc: EvidenceDoc) -> str:
        self._docs[doc.id] = doc
        return doc.id

    def all_docs(self) -> List[EvidenceDoc]:
        return sorted(self._docs.values(), key=lambda d: d.ingested_at, reverse=True)


store = EvidenceStore()


def ingest_document(title: str, content: str, source_type: str) -> str:
    doc = EvidenceDoc(
        id=str(uuid.uuid4()),
        title=title,
        content=content,
        source_type=source_type,
        ingested_at=datetime.utcnow(),
    )
    return store.add(doc)


def answer_question(question: str, max_sources: int = 3) -> tuple[str, List[EvidenceSnippet]]:
    docs = store.all_docs()[:max_sources]

    evidence: List[EvidenceSnippet] = []
    for d in docs:
        snippet = d.content[:260].replace("\n", " ")
        evidence.append(
            EvidenceSnippet(
                document_id=d.id,
                title=d.title,
                quoted_text=snippet,
            )
        )

    if not docs:
        answer = "No evidence documents are loaded in the demo store yet."
    else:
        titles = ", ".join(d.title for d in docs)
        answer = (
            "This is a hackathon friendly placeholder answer grounded in "
            f"{len(docs)} source documents: {titles}. "
            "In a full build you would call the Pathway LLM xPack with these snippets "
            "as retrieval context to synthesize a clinically styled answer."
        )

    return answer, evidence
