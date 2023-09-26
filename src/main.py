from pydantic import BaseModel

from fastapi import FastAPI, Request, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware


class ParseAndCompileRequest(BaseModel):
    xml: str


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://chat.openai.com",
        "http://localhost:8000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/parse_and_compile")
async def compile(request: ParseAndCompileRequest):
    # TODO
    return {"response": "parsed and compiled XML successfully!"}

app.mount("/", StaticFiles(directory="public"), name="public")
