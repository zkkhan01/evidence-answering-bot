from datetime import datetime
from fastapi import APIRouter

from ..schemas import (
    IngestDocumentRequest,
    IngestDocumentResponse,
    AskQuestionRequest,
    AnswerResponse,
)
from ..pipeline import ingest_document, answer_question

router = APIRouter(prefix="/evidence", tags=["evidence"])  # type: ignore


@router.post("/ingest", response_model=IngestDocumentResponse)
async def ingest(payload: IngestDocumentRequest) -> IngestDocumentResponse:
    doc_id = ingest_document(
        title=payload.title,
        content=payload.content,
        source_type=payload.source_type,
    )
    return IngestDocumentResponse(document_id=doc_id)


@router.post("/ask", response_model=AnswerResponse)
async def ask(payload: AskQuestionRequest) -> AnswerResponse:
    answer, evidence = answer_question(
        question=payload.question,
        max_sources=payload.max_sources,
    )
    return AnswerResponse(
        question=payload.question,
        answer=answer,
        generated_at=datetime.utcnow(),
        evidence=evidence,
    )
