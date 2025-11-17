from datetime import datetime
from pydantic import BaseModel
from typing import List


class IngestDocumentRequest(BaseModel):
    source_type: str  # guideline, trial, meta_analysis
    title: str
    content: str


class IngestDocumentResponse(BaseModel):
    document_id: str


class AskQuestionRequest(BaseModel):
    question: str
    max_sources: int = 3


class EvidenceSnippet(BaseModel):
    document_id: str
    title: str
    quoted_text: str


class AnswerResponse(BaseModel):
    question: str
    answer: str
    generated_at: datetime
    evidence: List[EvidenceSnippet]
