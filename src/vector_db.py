import chromadb
from sentence_transformers import SentenceTransformer

from . import config


class VectorDB:
    def __init__(self, path, chunks=None):
        self._client = chromadb.PersistentClient(path=path)
        existing = {c.name for c in self._client.list_collections()}

        if config.COLLECTION_NAME in existing:
            print(f"[VectorDB] Reloading existing collection at '{path}'...")
            self._collection = self._client.get_collection(config.COLLECTION_NAME)
            embedding_model = self._collection.metadata["embedding_model"]
            print(f"[VectorDB] Loading embedding model '{embedding_model}'...")
            self._model = SentenceTransformer(embedding_model)
            print(f"[VectorDB] Reloaded {self._collection.count()} chunks.")
        elif chunks:
            print(f"[VectorDB] No collection found at '{path}', creating one...")
            print(f"[VectorDB] Loading embedding model '{config.EMBEDDING_MODEL}'...")
            self._model = SentenceTransformer(config.EMBEDDING_MODEL)
            self._collection = self._client.get_or_create_collection(
                name=config.COLLECTION_NAME,
                metadata={"embedding_model": config.EMBEDDING_MODEL},
            )
            print(f"[VectorDB] Encoding and indexing {len(chunks)} chunks...")
            self._index(chunks)
            print("[VectorDB] Done.")
        else:
            raise ValueError(
                f"No collection '{config.COLLECTION_NAME}' at '{path}' "
                "and no chunks provided to create one."
            )

    def _encode(self, texts):
        return self._model.encode(
            texts, batch_size=32, normalize_embeddings=True, show_progress_bar=True
        ).tolist()

    def _index(self, chunks):
        self._collection.add(
            ids=[c["id"] for c in chunks],
            documents=[c["text"] for c in chunks],
            embeddings=self._encode([c["text"] for c in chunks]),
            metadatas=[{"source": c["source"]} for c in chunks],
        )
