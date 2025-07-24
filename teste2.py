# Função que dobra um número
def dobrar(numero):
    return numero * 2

# Exemplo de uso
resultado = dobrar(5)
print(f"O dobro de 5 é: {resultado}")

# Definindo a classe Pessoa
class Pessoa:
    def __init__(self, nome, idade):  # Método especial __init__
        self.nome = nome              # Atributos
        self.idade = idade

    def apresentar(self):             # Método comum
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."

# Criando uma instância da classe
p1 = Pessoa("Kaue", 20)

# Acessando método da classe
print(p1.apresentar())

