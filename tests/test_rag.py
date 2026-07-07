from src.rag import build_system_prompt

TEMPLATE = "Contexte :\n{{Chunks}}\nFin."

CHUNKS = [
    {"text": "Le chat bleu de Bob s'appelle Henri.", "metadata": {"source": "carnet_de_bob"}},
    {"text": "Le chien vert d'Alice s'appelle Gaston.", "metadata": {"source": "registre_animalier"}},
]


def test_build_system_prompt_replaces_placeholder():
    prompt = build_system_prompt(TEMPLATE, CHUNKS)

    assert "{{Chunks}}" not in prompt
    assert "1. Le chat bleu de Bob s'appelle Henri. (source: carnet_de_bob)" in prompt
    assert "2. Le chien vert d'Alice s'appelle Gaston. (source: registre_animalier)" in prompt


def test_build_system_prompt_keeps_surrounding_text():
    prompt = build_system_prompt(TEMPLATE, CHUNKS)

    assert prompt.startswith("Contexte :\n")
    assert prompt.endswith("\nFin.")
