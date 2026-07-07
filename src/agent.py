from dotenv import load_dotenv
from groq import Groq


class Agent:
    def __init__(self):
        load_dotenv()
        self.client = Groq()

    @staticmethod
    def read_file(path):
        with open(path, encoding="utf-8") as f:
            return f.read()
