from fastapi import APIRouter

router = APIRouter(
    prefix="/api/v1/matches",
    tags=["Matches"]
)


@router.post("/")
async def create_match(
    resume_id: str,
    job_id: str
):
    return {
        "message": "Create match",
        "resume_id": resume_id,
        "job_id": job_id
    }


@router.get("/")
async def get_matches():
    return {"message": "Get matches"}


@router.get("/{match_id}")
async def get_match(match_id: str):
    return {
        "message": "Get match",
        "match_id": match_id
    }