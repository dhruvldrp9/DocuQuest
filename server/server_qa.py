from fastapi import FastAPI
from helper_text_gen import api_ans

app = FastAPI()


@app.post("/")
async def process_text(data: dict):
    """
    This endpoint processes a document (doc) and an answer (answer) using the text_gen.api_ans function.
    """
    question = data.get("question")
    result = api_ans(question)
    return {"result": result}
