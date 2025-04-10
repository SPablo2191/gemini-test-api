from dotenv import load_dotenv
from google import genai
import os


# cargar variables de entorno y constantes
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
SYSTEM_PROMPT= """Todo respuesta que obtengas lo traduces al ingles. Redactalo en un solo parrafo, breve y conciso."""


# creamos una instancia de cliente (el equivalente a nuestro administrador de modelos y funcionalidades de geminiAI)
client = genai.Client(api_key=API_KEY)