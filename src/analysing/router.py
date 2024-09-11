from fastapi import APIRouter, Body, HTTPException, status
from src.analysing import service
from bson import ObjectId

router = APIRouter()

@router.post("/analyse_strength_weakness")
async def analyse_strength_weakness(file_url: str = Body(...)):
    cv_content = service.load_pdf(file_url=file_url)
    
    strength = service.analysing_strength(cv_content=cv_content)
    weakness = service.analysing_weakness(cv_content=cv_content)
    
    return [strength, weakness]