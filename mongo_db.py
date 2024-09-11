from pymongo import MongoClient
import os

client = MongoClient(os.getenv("MONGODB_URI"))
db = client["database"]

def connectUser():
    users_collection = db["users"]
    return users_collection

def connectAnalysis():
    analysis_collection = db["analysis"]
    return analysis_collection

def connectJob():
    job_collection = db["jobs"]
    return job_collection

def connectMatch():
    match_collection = db["matchings"]
    return match_collection

