def build_system_prompt(template, chunks):
    formatted_chunks = "\n".join(
        f"{i}. {chunk['text']} (source: {chunk['metadata']['source']})"
        for i, chunk in enumerate(chunks, start=1)
    )
    return template.replace("{{Chunks}}", formatted_chunks)
