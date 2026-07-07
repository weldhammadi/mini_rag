from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel

from src import config
from src.corpus import load_chunks
from src.rag import RAG
from src.vector_db import VectorDB

rag = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    global rag
    VectorDB(config.CHROMA_PATH, chunks=load_chunks())
    rag = RAG()
    yield


app = FastAPI(lifespan=lifespan)


class Question(BaseModel):
    question: str


@app.get("/")
async def index():
    return FileResponse("static/index.html")


@app.post("/ask")
async def ask(payload: Question):
    return {"answer": rag.answer_question(payload.question)}
