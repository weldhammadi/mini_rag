# mini_rag

Mini-RAG minimal mais complet — ChromaDB + sentence-transformers + Groq + agent modérateur.
TP guidé M2 MD5 (voir [tp.md](tp.md) pour l'énoncé complet), maintenant exposé via une petite API web et déployable sur Railway.

## Architecture

Trois briques, chacune dans son propre fichier, plus config et prompts séparés du code, plus une couche web additive :

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
| `main.py` | Script de démo CLI (questions du §6 du tp.md) | ✅ vérifié bout en bout |
| `api.py` | API FastAPI (`GET /`, `POST /ask`) servant la même `RAG` | ✅ |
| `static/index.html` | UI web minimale (HTML/CSS/JS vanilla, sans framework) | ✅ |
| `Procfile` | Commande de démarrage Railway (`uvicorn`) | ✅ |
| `tests/test_vector_db.py` | 4 tests : création, reload, erreur, retrieve | ✅ |
| `tests/test_moderator.py` | 2 tests : question légitime, injection | ✅ |
| `tests/test_rag.py` | 5 tests : templating, réponse correcte, refus injection, hors périmètre | ✅ |
| `tests/test_api.py` | 1 test : `POST /ask` bout en bout | ✅ |

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

## Lancer la démo CLI

```bash
python main.py
```

## Lancer l'API web en local

```bash
python -m uvicorn api:app --reload
```

Puis ouvrir `http://127.0.0.1:8000/`.

## Déploiement Railway

Le code est prêt (`Procfile` + `requirements.txt`), mais deux réglages se font uniquement depuis le dashboard/CLI Railway (pas depuis le code) :

1. **Variable d'environnement** : ajouter `GROQ_API_KEY` dans les variables du service Railway (Settings → Variables).
2. **Volume persistant** : attacher un Volume Railway monté sur le chemin `chroma_db/` de l'app (typiquement `/app/chroma_db`) — sinon la base ChromaDB est reconstruite depuis `data/05_corpus_rag.csv` à chaque redémarrage/redeploy au lieu d'être rechargée. `VectorDB` gère déjà l'un ou l'autre cas automatiquement (voir `src/vector_db.py`), aucun code à changer.

Une fois ces deux réglages faits, Railway détecte le `Procfile` et lance `uvicorn api:app --host 0.0.0.0 --port $PORT` automatiquement à chaque déploiement.
