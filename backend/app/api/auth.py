from fastapi import APIRouter

router = APIRouter(
    prefix="/api/v1/auth",
    tags=["Authentication"]
)


@router.post("/register")
async def register():
    return {"message": "Register endpoint"}


@router.post("/login")
async def login():
    return {"message": "Login endpoint"}


@router.get("/me")
async def get_current_user():
    return {"message": "Current user endpoint"}