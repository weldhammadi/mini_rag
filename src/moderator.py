import json

from . import config
from .agent import Agent


class Moderator(Agent):
    def moderate(self, question):
        chat_completion = self.client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": Agent.read_file(config.MODERATOR_SYSTEM_PROMPT_PATH),
                },
                {"role": "user", "content": question},
            ],
            model=config.MODERATION_MODEL,
            response_format={"type": "json_object"},
            temperature=0,
        )
        return json.loads(chat_completion.choices[0].message.content)
