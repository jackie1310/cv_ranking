from fastapi import APIRouter, HTTPException, status
from src.matching import service
from src.matching.schemas import MatchingSchema, ResponseSchema, JobSchema
from mongo_db import connectMatch
from bson import ObjectId

router = APIRouter()


match_collection = connectMatch()
@router.post("/analyse")
async def analyse_matching(matching_data: MatchingSchema):
    result = service.analyse_matching(matching_data=matching_data)
    
    matching_document = {
        "job_id": matching_data.job["_id"],
        "candidate_id": matching_data.candidate["_id"],
        "certificate": result["certificate"],
        "degree": result["degree"],
        "experience": result["experience"],
        "responsibility": result["responsibility"],
        "score": result["score"],
        "soft_skill": result["soft_skill"],
        "summary_comment": result["summary_comment"],
        "technical_skill": result["technical_skill"]
    }
    
    match_collection.insert_one(matching_document)
    return "Matched"

@router.get("/get_matchings/{job_id}")
async def get_content(job_id: str):
    
    # Attempt to find the document with the matching job_id
    results = match_collection.find({"job_id": job_id})
    results_list = list(results)
    
    if not results_list:
        # If no document is found, raise a 404 error
        return "Not Found"
    
    # Return the found document (result is a dictionary and can be serialized to JSON)
    for result in results_list:
        if '_id' in result:
            result['_id'] = str(result['_id'])
    
    # Return the found document (result is a dictionary and can be serialized to JSON)
    return results_list

@router.delete("/delete_matching")
async def delete_matching(job_id: str, candidate_id: str):
    result = match_collection.delete_one({"job_id": job_id, "candidate_id": candidate_id})
    
    if result.deleted_count == 1:
        return {"message": "Matching deleted successfully"}
    else:
        raise HTTPException(status_code=402, detail="Matching not found")
    
# @router.delete("/test_matching")
# async def test_matching(job_id: str, candidate_id: str):
#     # result = match_collection.delete_one({"job_id": job_id, "candidate_id": candidate_id})
    
#     # if result.deleted_count == 1:
#     #     return {"message": "Matching deleted successfully"}
#     # else:
#     #     raise HTTPException(status_code=404, detail="Matching not found")
#     return {"job_id": job_id, "candidate_id": candidate_id}