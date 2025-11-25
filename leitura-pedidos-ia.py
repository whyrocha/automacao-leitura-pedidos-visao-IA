import os
import csv
import base64
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

IMAGENS_DIR = "automacao_pedido/imagens_pedidos"

ARQUIVO_SAIDA = r"automacao_pedido\pedidos.csv"


# envia a imagem pro modelo de visão e retorna dicts
def imagem_para_itens(caminho_imagem: str):
    """Envia a imagem para o modelo de visão e retorna lista de dicts:
       [{"codigo": "...", "qnt": 1}, ...]
    """
    with open(caminho_imagem, "rb") as f:
        b64 = base64.b64encode(f.read()).decode("utf-8")

    img_url = f"data:image/jpeg;base64,{b64}"

    prompt = (
        "Você é um assistente que lê pedidos escritos à mão. "
        "Na imagem há vários códigos de produtos (mistura de letras e números) "
        "e, à direita de cada código, um número dentro de um círculo indicando a quantidade.\n\n"
        "Extraia TODOS os itens da imagem e responda SOMENTE em linhas CSV, "
        "no formato: codigo,quantidade\n"
        "Exemplo de saída:\n"
        "4PK0980,1\n"
        "IKS4305,2\n"
        "Não escreva nenhum texto extra, só as linhas CSV."
    )

    response = client.chat.completions.create(
        model="gpt-4.1-mini",  # ou gpt-4.1 / gpt-4.1-mini / gpt-5.1 etc
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {"type": "image_url", "image_url": {"url": img_url}},
                ],
            }
        ],
    )

    csv_text = response.choices[0].message.content.strip()
    itens = []

    for linha in csv_text.splitlines():
        partes = [p.strip() for p in linha.split(",")]
        if len(partes) != 2:
            continue
        codigo, qnt = partes
        # pequena limpeza
        codigo = codigo.replace(" ", "").upper()
        try:
            qnt = int(qnt)
        except ValueError:
            continue
        itens.append({"codigo": codigo, "qnt": qnt})

    return itens


# lê e processa as imagens
def processar_pasta():
    todos_itens = []

    for nome_arquivo in os.listdir(IMAGENS_DIR):
        if not nome_arquivo.lower().endswith((".jpg", ".jpeg", ".png")):
            continue

        caminho = os.path.join(IMAGENS_DIR, nome_arquivo)
        print(f"Lendo {caminho}...")
        itens = imagem_para_itens(caminho)
        for item in itens:
            item["origem_imagem"] = nome_arquivo 
        todos_itens.extend(itens)

    if not todos_itens:
        print("Nenhum item lido.")
        return

    with open(ARQUIVO_SAIDA, "w", newline="", encoding="utf-8") as f:
        campos = ["codigo", "qnt", "origem_imagem"]
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()
        writer.writerows(todos_itens)

    print(f"Arquivo '{ARQUIVO_SAIDA}' gerado com {len(todos_itens)} linhas.")


if __name__ == "__main__":
    processar_pasta()
    