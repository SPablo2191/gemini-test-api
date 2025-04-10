from google import genai
from google.genai import types

# solicito la api key por consola
api_key = input("ingrese su api key: ")

# creamos una instancia de cliente (el equivalente a nuestro administrador de modelos y funcionalidades de geminiAI)
client = genai.Client(api_key=api_key)

# habilito la terminal para que el usuario pueda hacer una pregunta
print("Conexión habilitada - Ya puede hacer una consulta a GeminiAI")
question = input(">")

# llamo a la API haciendo uso de un modelo en particular, y pasandole el prompt
response = client.models.generate_content(
    model="gemini-2.0-flash", contents=question, config=types.GenerateContentConfig(
        system_instruction="Todo respuesta que obtengas lo traduces al ingles",
        # max_output_tokens=3,
        temperature=0.3,
    ),
)

# mostramos la respuesta
print(response.text)
