from fastapi import APIRouter, Body, HTTPException, status
from src.job import service
from src.job.schemas import JobSchema, ResponseSchema
from mongo_db import connectJob
from bson import ObjectId

router = APIRouter()

job_collection = connectJob()
# @router.post("/analyse", response_model=ResponseSchema)
@router.post("/analyse")
async def analyse_job(job_data: JobSchema):
    result = service.analyse_job(job_data=job_data)
    
    job_document = {
        "job_name": job_data.job_name,
        "degree": result["degree"],
        "experience": result["experience"],
        "technical_skill": result["technical_skill"],
        "responsibility": result["responsibility"],
        "certificate": result["certificate"],
        "soft_skill": result["soft_skill"]
    }
    
    job_collection.insert_one(job_document)

    return result
    # return {"job_name": job_data.job_name, "job_description": job_data.job_description}

@router.post("/read_job")
async def analyse_job(job_data: JobSchema):
    return {"job_name": job_data.job_name, "job_description": job_data.job_description}

@router.get("/get_all_jobs")
def get_all_jobs():
    jobs_list = []
    for job in job_collection.find():
        job["_id"] = str(job["_id"])
        jobs_list.append(job)
    
    return jobs_list

@router.delete("/delete_job/{_id}", status_code=status.HTTP_200_OK)
def delete_analysis(_id: str):
    job_collection = connectJob()
    
    # Convert _id to ObjectId if necessary
    try:
        object_id = ObjectId(_id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid ID format")
    
    # Attempt to delete the document
    result = job_collection.delete_one({"_id": object_id})
    
    if result.deleted_count == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Analysis not found")
    
    return {"message": "Job Deleted"}