import csv

from . import config


def load_chunks():
    with open(config.CORPUS_CSV_PATH, encoding="utf-8") as f:
        return list(csv.DictReader(f))
