from typing import Union
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from src.candidate.router import router as candidate_router
from src.candidate.auth import router as candidate_auth
from config import settings
from src.job.router import router as job_router
from src.matching.router import router as matching_router

app = FastAPI(title=settings.APP_NAME)  

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://cv-ranking-front-end.vercel.app", "https://cybersoft-cv-ranking.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Message": "Welcome to Cybersoft"}

@app.get("/healthz")
async def healthcheck() -> bool:
    return True

# @app.post("/upload")
# async def upload_file(file: UploadFile = File(...)):
#     try:
#         bucket = storage.bucket()
#         blob = bucket.blob(f"{uuid.uuid4()}_{file.filename}")

#         # Upload the file to Firebase Storage
#         blob.upload_from_file(file.file, content_type=file.content_type)

#         # Get the file's public URL
#         file_url = blob.public_url

#         return {"filename": file.filename, "url": file_url}

#     except Exception as e:
#         return {"error": str(e)}

app.include_router(candidate_router, prefix="/candidate", tags=["Candidate"])
app.include_router(candidate_auth, prefix="/auth", tags=["Auth"])
app.include_router(job_router, prefix="/job", tags=["Job"])
app.include_router(matching_router, prefix="/matching", tags=["Matching"])