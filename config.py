from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

EMBEDDING_MODEL = "distiluse-base-multilingual-cased-v2"
LLM_MODEL = "llama-3.3-70b-versatile"
MODERATION_MODEL = "openai/gpt-oss-safeguard-20b"

CHROMA_PATH = str(BASE_DIR / "chroma_db")
COLLECTION_NAME = "toy_corpus"
N_RESULTS = 3

CORPUS_CSV_PATH = BASE_DIR / "data" / "05_corpus_rag.csv"

RAG_SYSTEM_PROMPT_PATH = BASE_DIR / "prompts" / "rag_system.txt"
MODERATOR_SYSTEM_PROMPT_PATH = BASE_DIR / "prompts" / "moderator_system.txt"
