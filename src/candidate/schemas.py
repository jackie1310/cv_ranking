from pydantic import BaseModel, Field
from fastapi import UploadFile, File, Form

class RequestSchema(BaseModel):
    email: str = Form(...)
    file: UploadFile = File(...)
    

class ResponseSchema(BaseModel):
    candidate_name: str
    phone_number: str
    email: str
    comment: str
    degree: list
    experience: list
    technical_skill: list
    responsibility: list
    certificate: list
    soft_skill: list
    job_recommended: list