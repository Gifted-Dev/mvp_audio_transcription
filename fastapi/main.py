from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse, JSONResponse
from transformers import pipeline
import os
import torch
import uuid
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph


app = FastAPI()


UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


# load the model
device = "cuda" if torch.cuda.is_available() else "cpu"
whisper_model = pipeline("automatic-speech-recognition", "openai/whisper-base", device=device)

# function to generate pdf
def generate_pdf(text: str, pdf_path: str):
    doc = SimpleDocTemplate(pdf_path, pagesize=letter)
    styles = getSampleStyleSheet()
    
    # Wrap text correctly
    formatted_text = Paragraph(text, styles["Normal"])

    doc.build([formatted_text])  # Build the PDF with wrapped text


tasks_db = {}

@app.post("/upload_files")
async def upload(file: UploadFile = File(...)):
    
    file_id = str(uuid.uuid4())
    file_extension = file.filename.strip(".")[-1]
    filename = f"{file_id}.{file_extension}"
        
    file_path = os.path.join(UPLOAD_DIR, filename)
    
    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())
        
        
    
    # Transcribe the model
    if file_extension == "mp3" or file_extension == "m4a":
        result = whisper_model(file_path, return_timestamps=True, generate_kwargs={"language": "en"})
        transcription_text = result['text']
    
    
    # Generate a PDF file with transcription
    pdf_filename = f"{file_id}.pdf"
    pdf_path = os.path.join(UPLOAD_DIR, pdf_filename)
    generate_pdf(transcription_text, pdf_path)
    
    
    # Add pdf path to task id
    tasks_db[file_id] = pdf_filename
    
    
    # Return transcripton + PDF download link
    return JSONResponse(
        content={
            "message": "Transcription completed!",
            "transcription": transcription_text,
            "pdf_download_link": f"/download/{file_id}"
        }
    )
    
@app.get("/download/{file_id}")
async def download_pdf(file_id: str):
    pdf_filename = tasks_db.get(file_id)
    
    if not pdf_filename:
        return JSONResponse(content={"error": "file not found"}, status_code=404)
    
    
    pdf_path = os.path.join(UPLOAD_DIR, pdf_filename)

    if not os.path.exists(pdf_path):
        return JSONResponse(content={"error": "File not found"}, status_code=404)

    return FileResponse(pdf_path, media_type="application/pdf", filename=pdf_filename)