# mini_rag

Mini-RAG minimal mais complet — ChromaDB + sentence-transformers + Groq + agent modérateur.
TP guidé M2 MD5 (voir [tp.md](tp.md) pour l'énoncé complet).

## Architecture

Trois briques, chacune dans son propre fichier, plus config et prompts séparés du code :

| Fichier | Rôle | Statut |
|---|---|---|
| `src/config.py` | Constantes (modèles, chemins) | ✅ |
| `src/corpus.py` | Charge le corpus depuis `data/05_corpus_rag.csv` | ✅ |
| `src/vector_db.py` | `VectorDB` — création/rechargement ChromaDB + `retrieve` | ✅ |
| `src/agent.py` | `Agent` — classe de base (client Groq, `read_file`) | ✅ |
| `src/moderator.py` | `Moderator(Agent)` — détection de prompt injection (JSON) | ✅ |
| `src/rag.py` | `RAG(Agent)` — orchestration (modération → retrieval → LLM) | ✅ |
| `prompts/moderator_system.txt` | Prompt système du modérateur | ✅ |
| `prompts/rag_system.txt` | Prompt système du RAG (`{{Chunks}}`) | ✅ |
| `main.py` | Script de démo bout en bout (questions du §6 du tp.md) | ✅ (écrit, vérification bloquée par une 403 réseau Groq ponctuelle) |
| `tests/test_vector_db.py` | 4 tests : création, reload, erreur, retrieve | ✅ |
| `tests/test_moderator.py` | 2 tests : question légitime, injection | ✅ |
| `tests/test_rag.py` | 5 tests : templating, réponse correcte, refus injection, hors périmètre | ✅ |

## Tests

```bash
pytest -v
```

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
