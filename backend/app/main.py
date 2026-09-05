from fastapi import FastAPI

from app.api.auth import router as auth_router
from app.api.resumes import router as resume_router
from app.api.jobs import router as job_router
from app.api.matches import router as match_router


app = FastAPI(
    title="AI Resume Job Matcher",
    version="1.0.0",
)


app.include_router(auth_router)
app.include_router(resume_router)
app.include_router(job_router)
app.include_router(match_router)


@app.get("/health")
async def health_check():
    return {
        "status": "ok"
    }