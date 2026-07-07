import pytest

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


def test_reload_uses_persisted_data_without_chunks(tmp_path):
    VectorDB(str(tmp_path), chunks=SAMPLE_CHUNKS)

    reloaded = VectorDB(str(tmp_path))

    assert reloaded._collection.count() == len(SAMPLE_CHUNKS)
    assert reloaded._model.get_embedding_dimension() > 0


def test_raises_without_existing_db_and_without_chunks(tmp_path):
    with pytest.raises(ValueError):
        VectorDB(str(tmp_path))


def test_retrieve_returns_closest_chunk_first(tmp_path):
    db = VectorDB(str(tmp_path), chunks=SAMPLE_CHUNKS)

    results = db.retrieve("Quelle est la couleur du chat de Bob ?", n=2)

    assert len(results) == 2
    assert results[0]["text"] == SAMPLE_CHUNKS[0]["text"]
    assert results[0]["metadata"]["source"] == SAMPLE_CHUNKS[0]["source"]
