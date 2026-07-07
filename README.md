# mini_rag

Mini-RAG minimal mais complet — ChromaDB + sentence-transformers + Groq + agent modérateur.
TP guidé M2 MD5 (voir [tp.md](tp.md) pour l'énoncé complet).

## Architecture

Trois briques, chacune dans son propre fichier, plus config et prompts séparés du code :

| Fichier | Rôle | Statut |
|---|---|---|
| `src/config.py` | Constantes (modèles, chemins) | ✅ |
| `src/corpus.py` | Charge le corpus depuis `data/05_corpus_rag.csv` | ✅ |
| `src/vector_db.py` | `VectorDB` — création/rechargement ChromaDB + `retrieve` | ⏳ (création faite, reload/retrieve à venir) |
| `src/moderator.py` | `Moderator` — détection de prompt injection (JSON) | ⏳ |
| `src/rag.py` | `RAG` — orchestration (modération → retrieval → LLM) | ⏳ |
| `prompts/*.txt` | Prompts système (RAG et modérateur) | ⏳ |
| `main.py` | Script de démo bout en bout | ⏳ |
| `tests/` | Tests unitaires (un fichier par brique) | ⏳ en cours |

## Installation

```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
pip install -r requirements.txt
cp .env.example .env    # puis renseigner GROQ_API_KEY
```

## Lancer la démo

```bash
python main.py
```
