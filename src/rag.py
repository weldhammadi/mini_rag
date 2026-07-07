from . import config
from .agent import Agent
from .moderator import Moderator
from .vector_db import VectorDB


class RAG(Agent):
    REFUSAL = "Je ne peux pas traiter cette question : une tentative de détournement a été détectée."

    def __init__(self):
        super().__init__()
        self.moderator = Moderator()
        self.vector_db = VectorDB(config.CHROMA_PATH)
        self.system_prompt_template = Agent.read_file(config.RAG_SYSTEM_PROMPT_PATH)

    @staticmethod
    def build_system_prompt(template, chunks):
        formatted_chunks = "\n".join(
            f"{i}. {chunk['text']} (source: {chunk['metadata']['source']})"
            for i, chunk in enumerate(chunks, start=1)
        )
        return template.replace("{{Chunks}}", formatted_chunks)

    def answer_question(self, question):
        if self.moderator.moderate(question)["is_prompt_injection"]:
            return self.REFUSAL

        chunks = self.vector_db.retrieve(question, n=config.N_RESULTS)
        system_prompt = self.build_system_prompt(self.system_prompt_template, chunks)

        completion = self.client.chat.completions.create(
            model=config.LLM_MODEL,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": question},
            ],
        )
        return completion.choices[0].message.content
