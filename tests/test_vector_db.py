from src import config
from src.vector_db import VectorDB

SAMPLE_CHUNKS = [
    {"id": "chunk_001", "text": "Le chat bleu de Bob s'appelle Henri.", "source": "carnet_de_bob"},
    {"id": "chunk_002", "text": "Le chien vert d'Alice s'appelle Gaston.", "source": "registre_animalier"},
    {"id": "chunk_003", "text": "La tortue orange de Carla se nomme Prosper.", "source": "registre_animalier"},
]


def test_create_indexes_all_chunks(tmp_path):
    db = VectorDB(str(tmp_path), chunks=SAMPLE_CHUNKS)

    assert db._collection.count() == len(SAMPLE_CHUNKS)
    assert db._collection.metadata["embedding_model"] == config.EMBEDDING_MODEL
