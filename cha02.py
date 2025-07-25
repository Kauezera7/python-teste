import psycopg2
from psycopg2 import OperationalError, Error

# Dados de conexão
host = "1"
port = "5"
database = "dev"
user = "usr"
password = "u"

try:
    
    conexao = psycopg2.connect(
        host=host,
        port=port,
        database=database,
        user=user,
        password=password
    )

   
    cursor = conexao.cursor()

    
    cursor.execute("SELECT * FROM avaliacao.funcionarios;")

  
    registros = cursor.fetchall()

    print(" Registros encontrados:")
    for registro in registros:
        print(registro)

except OperationalError as e:
    print(f" Erro na conexão com o banco: {e}")

except Error as e:
    print(f" Erro ao executar a consulta: {e}")
finally:
   
    if 'cursor' in locals():
        cursor.close()
    if 'conexao' in locals():
        conexao.close()
    print("🔒 Conexão encerrada.")
