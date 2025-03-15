from fastapi import FastAPI
from refactor_engine import RefactorEngine

app = FastAPI()

@app.post("/refactor/")
async def refactor_code(code: str):
    return {"refactored_code": RefactorEngine(code).refactor_code()}
