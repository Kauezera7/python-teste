import psycopg2
from psycopg2 import OperationalError

class ConexaoBanco:
    def __init__(self, host, port, database, user, password):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.conexao = None

    def conectar(self):
        try:
            self.conexao = psycopg2.connect(
                host=self.host,
                port=self.port,
                database=self.database,
                user=self.user,
                password=self.password
            )
            print("Conexão com o banco de dados bem-sucedida!")
        except OperationalError as e:
            print(f" Erro ao conectar no banco de dados: {e}")

    def fechar_conexao(self):
        if self.conexao:
            self.conexao.close()
            print(" Conexão encerrada com sucesso.")

    def executar_consulta(self, consulta):
        try:
            with self.conexao.cursor() as cursor:
                cursor.execute(consulta)
                resultado = cursor.fetchall()
                return resultado
        except Exception as e:
            print(f"Erro ao executar a consulta: {e}")
            return None
