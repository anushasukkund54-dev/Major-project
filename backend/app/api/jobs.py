from fastapi import APIRouter

router = APIRouter(
    prefix="/api/v1/jobs",
    tags=["Jobs"]
)


@router.get("/search")
async def search_jobs(
    query: str,
    location: str | None = None
):
    return {
        "message": "Job search endpoint",
        "query": query,
        "location": location
    }


@router.get("/{job_id}")
async def get_job(job_id: str):
    return {
        "message": "Get job",
        "job_id": job_id
    }