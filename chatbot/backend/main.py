from fastapi import FastAPI
from pydantic import BaseModel

# Initialize FastAPI app
app = FastAPI(
    title="Event Chatbot API",
    description="Backend for AI chatbot to analyze event data from BigQuery",
    version="0.1.0"
)

# Define request model for user question
class QuestionRequest(BaseModel):
    question: str

# Define response model
class QuestionResponse(BaseModel):
    message: str

# Endpoint to handle user questions
@app.post("/api/ask", response_model=QuestionResponse)
async def ask_question(request: QuestionRequest):
    """
    Receives a user question and returns a placeholder response.
    Later, this will integrate with Gemini and BigQuery.
    
    Args:
        request (QuestionRequest): JSON payload with user question
        
    Returns:
        QuestionResponse: JSON response with a message
    """
    question = request.question
    return QuestionResponse(message=f"Received question: {question}")

# Run the app (for testing locally)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)