import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=r'C:\Users\Vitor Brandão\Desktop\Vitor\Projetos Data Science\Chatbot - Leitura de Documentos de Texto\venv\.env')

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
