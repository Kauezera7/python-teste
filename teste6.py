import psycopg2
from psycopg2 import OperationalError, Error

# Dados de conexão
host = "1"
port = "5"
database = "dev"
user = "usr"
password = "u"

try:
    # Estabelece conexão com o banco
    conexao = psycopg2.connect(
        host=host,
        port=port,
        database=database,
        user=user,
        password=password
    )

    # Cria cursor para executar comandos SQL
    cursor = conexao.cursor()

    # Executa consulta na tabela avaliacao.funcionarios
    cursor.execute("SELECT * FROM avaliacao.funcionarios;")

    # Busca todos os registros
    registros = cursor.fetchall()

    print("✅ Registros encontrados:")
    for registro in registros:
        print(registro)

except OperationalError as e:
    print(f"❌ Erro na conexão com o banco: {e}")

except Error as e:
    print(f"❌ Erro ao executar a consulta: {e}")

finally:
    # Fecha cursor e conexão para liberar recursos
    if 'cursor' in locals():
        cursor.close()
    if 'conexao' in locals():
        conexao.close()
    print("🔒 Conexão encerrada.")
