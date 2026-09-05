from fastapi import APIRouter

router = APIRouter(
    prefix="/api/v1/resumes",
    tags=["Resumes"]
)


@router.post("/")
async def upload_resume():
    return {"message": "Resume upload endpoint"}


@router.get("/")
async def get_resumes():
    return {"message": "Get resumes"}


@router.get("/{resume_id}")
async def get_resume(resume_id: str):
    return {
        "message": "Get resume",
        "resume_id": resume_id
    }


@router.delete("/{resume_id}")
async def delete_resume(resume_id: str):
    return {
        "message": "Delete resume",
        "resume_id": resume_id
    }