
# from fastapi import FastAPI
# from pydantic import BaseModel
# from agent_tools import generate_report

# app = FastAPI()

# class ResearchRequest(BaseModel):
#     topic: str

# @app.post("/analyze/")
# async def analyze(req: ResearchRequest):
#     report = generate_report(req.topic)
#     return report
from fastapi import FastAPI
from pydantic import BaseModel
from agent_tools import generate_report

app = FastAPI()

class ResearchRequest(BaseModel):
    topic: str

@app.post("/analyze/")
async def analyze(req: ResearchRequest):
    return generate_report(req.topic)
