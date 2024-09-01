# import firebase_admin
# from firebase_admin import credentials, storage
# import uuid
# from docx2pdf import convert

# cred = credentials.Certificate("credential.json")
# firebase_admin.initialize_app(cred, {
#     'storageBucket': "bcu-study-spaces.appspot.com"
# })

# bucket = storage.bucket()

# def is_docx(file_name):
#     return file_name.lower().endswith('.docx')

# def convert_docx_to_pdf(file_name):
#     # Convert the .docx file to .pdf
#     file_pdf = file_name.replace('.docx', '.pdf')
#     convert(file_name, file_pdf)
#     return file_pdf

# def delete_file_from_folder(folder_name, filename):
#     # Create the full path to the file in Firebase Storage
#     file_path = f'{folder_name}/{filename}'
    
#     # Get a reference to the blob (file) you want to delete
#     blob = bucket.blob(file_path)
    
#     # Delete the file
#     blob.delete()
    
#     # print(f'File {filename} deleted from folder {folder_name}')

# # Example usage
# def upload_file_to_firebase(email, file):
#     try:
#         if is_docx(file.filename):
#             file.filename = convert_docx_to_pdf(file.filename)
#         unique_filename = f"{uuid.uuid4()}_{file.filename}"
#         blob = bucket.blob(f"{email}/{unique_filename}")

#         # Upload the file to Firebase Storage
#         blob.upload_from_file(file.file, content_type=file.content_type)

#         # Get the file's public URL
#         blob.make_public()
#         file_url = blob.public_url
#         # file_url = blob.generate_signed_url(expires_in=60*60*24*30)

#         return file_url

#     except Exception as e:
#         return {"error": str(e)}

import firebase_admin
from firebase_admin import credentials, storage
import uuid
from docx2pdf import convert
import os
import subprocess

cred = credentials.Certificate("credential.json")
firebase_admin.initialize_app(cred, {
    'storageBucket': "bcu-study-spaces.appspot.com"
})

bucket = storage.bucket()

def is_docx(file_name):
    return file_name.lower().endswith('.docx')

def convert_docx_to_pdf(file_name):
    # Convert the .docx file to .pdf
    file_pdf = file_name.replace('.docx', '.pdf')
    convert(file_name, file_pdf)
    # subprocess.run(["docx2pdf", file_name, file_pdf], check=True)
    return file_pdf

def delete_file_from_folder(folder_name, filename):
    # Create the full path to the file in Firebase Storage
    file_path = f'{folder_name}/{filename}'
    
    # Get a reference to the blob (file) you want to delete
    blob = bucket.blob(file_path)
    
    # Delete the file
    blob.delete()

def upload_file_to_firebase(email, file):
    try:
        # Save the uploaded file to a temporary location
        # temp_file_path = f"docx/{file.filename}"
        # temp_file_path = os.path.join("/tmp", f"{uuid.uuid4()}_{file.filename}")
        # with open(temp_file_path, "wb") as temp_file:
        #     temp_file.write(file.file.read())
        # file.file.save(temp_file_path)
        
        # if is_docx(temp_file_path):
        #     # Convert .docx to .pdf
        #     converted_file_path = convert_docx_to_pdf(temp_file_path)
        # else:
        #     converted_file_path = temp_file_path
        
        # Generate a unique filename
        unique_filename = f"{uuid.uuid4()}_{file.filename}"
        blob = bucket.blob(f"{email}/{unique_filename}")

        # Upload the file to Firebase Storage
        blob.upload_from_file(unique_filename)

        # Get the file's public URL
        blob.make_public()
        file_url = blob.public_url

        return file_url

    except Exception as e:
        return {"error": str(e)}

    # finally:
    #     # Clean up the temporary files
    #     if temp_file_path:
    #         os.remove(temp_file_path)
    #     if converted_file_path and converted_file_path != temp_file_path:
    #         os.remove(converted_file_path)

# Example usage
# Assume `file` is an object with attributes `filename` and `file` (file content).
# The `email` is the user's email.
