from fastapi import FastAPI
from .routers import evidence

app = FastAPI(
    title="Evidence Answering Bot API",
    description="Track 3 - Evidence Answering for Clinicians with Pathway as live corpus",
    version="0.2.0",
)

app.include_router(evidence.router)


@app.get("/health")
async def health():
    return {"status": "ok"}
