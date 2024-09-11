from fastapi import APIRouter, Body, HTTPException, status
from src.candidate import service
from mongo_db import connectAnalysis
from bson import ObjectId

router = APIRouter()


# @router.post("/analyse", response_model=ResponseSchema)
@router.post("/analyse")
async def analyse_candidate(file_url: str = Body(...)):
    # if file.content_type != 'application/json':
    #     raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Wow, That's not allowed")

    # file_name = await service.save_cv_candidate(file=file)
    # file_url = upload_file_to_firebase(email=email, file=file)
        
    cv_content = service.load_pdf(file_url=file_url)

    result = service.analyse_candidate(cv_content=cv_content)
    
    analysis_collection = connectAnalysis()
    
    candidate_document = {
        "candidate_name": result["candidate_name"],
        "certificate": result["certificate"],
        "comment": result["comment"],
        "degree": result["degree"],
        "email": result["email"],
        "experience": result["experience"],
        "job_recommended": result["job_recommended"],
        "office": result["office"],
        "phone_number": result["phone_number"],
        "responsibility": result["responsibility"],
        "soft_skill": result["soft_skill"],
        "sql": result["sql"],
        "technical_skill": result["technical_skill"]
    }
    
    analysis_collection.insert_one(candidate_document)

    return result


# @router.post("/upload")
# async def upload_file(email: str = Form(...), file: UploadFile = File(...)):
#     file_url = upload_file_to_firebase(email=email, file=file.file)
#     return file_url

@router.get("/get_all_analysis")
def get_all_analysis():
    analysis_collection = connectAnalysis()
    list_of_analysis = []
    for analysis in analysis_collection.find():
        analysis['_id'] = str(analysis['_id']) 
        list_of_analysis.append(analysis)
        
    return list_of_analysis


@router.delete("/delete_analysis/{_id}", status_code=status.HTTP_200_OK)
def delete_analysis(_id: str):
    analysis_collection = connectAnalysis()
    
    # Convert _id to ObjectId if necessary
    try:
        object_id = ObjectId(_id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid ID format")
    
    # Attempt to delete the document
    result = analysis_collection.delete_one({"_id": object_id})
    
    if result.deleted_count == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Analysis not found")
    
    return {"message": "Analysis Deleted"}