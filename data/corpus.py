import csv

from config import CORPUS_CSV_PATH


def load_chunks():
    with open(CORPUS_CSV_PATH, encoding="utf-8") as f:
        return list(csv.DictReader(f))
