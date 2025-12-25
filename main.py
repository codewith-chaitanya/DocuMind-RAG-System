import uvicorn
from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from typing import List

app = FastAPI()

# input model
class QueryRequest(BaseModel):
    query_text: str

# output model
class QueryResponse(BaseModel):
    answer: str
    sources: List[str]

@app.get("/")
def home():
    # check if server is alive
    return {"message": "api is working"}

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    # validation
    if not file.filename.endswith(".pdf"):
        return {"error": "not a pdf file"}
    
    print("uploaded:", file.filename) # debug
    
    # TODO: extract text using pypdf
    # TODO: generate embeddings here
    
    return {"status": "received", "file": file.filename}

@app.post("/ask", response_model=QueryResponse)
async def ask_question(request: QueryRequest):
    print("query:", request.query_text)
    
    # logic for RAG pipeline:
    # 1. get vector from query
    # 2. search faiss
    # 3. call gemini api
    
    # dummy data for testing
    return QueryResponse(
        answer="LLM integration pending...",
        sources=["doc_1", "doc_2"]
    )

if __name__ == "__main__":
    # running on port 8000
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
