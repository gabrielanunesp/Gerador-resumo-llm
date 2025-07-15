import os
from openai import OpenAI

# Defina sua chave de API como variável de ambiente no seu sistema operacional para maior segurança.
# Exemplo no terminal (Windows PowerShell):
# setx OPENAI_API_KEY "sua-chave-aqui"

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def gerar_resumo(texto):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Você é um assistente que gera resumos."},
            {"role": "user", "content": f"Resuma o seguinte texto:\n{texto}"}
        ]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    texto_exemplo = """Seu texto longo aqui para testar o resumo."""
    resumo = gerar_resumo(texto_exemplo)
    print("Resumo gerado:\n", resumo)
