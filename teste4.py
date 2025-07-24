import requests

url = "https://the-internet.herokuapp.com/login"

try:
    # Envia requisição GET
    resposta = requests.get(url, timeout=5)

    # Verifica se a resposta foi bem-sucedida
    if resposta.status_code == 200:
        print("✅ Requisição bem-sucedida!")
        print("📄 Conteúdo da página (trecho):")
        print(resposta.text[:500])  # Mostra os primeiros 500 caracteres do HTML
    else:
        print(f"⚠️ Erro HTTP: Código {resposta.status_code}")

except requests.exceptions.ConnectionError:
    print("❌ Erro: Não foi possível conectar ao site (Problema de conexão).")

except requests.exceptions.Timeout:
    print("⏳ Erro: Tempo de conexão esgotado.")

except requests.exceptions.RequestException as erro:
    print(f"🚨 Erro inesperado: {erro}")
