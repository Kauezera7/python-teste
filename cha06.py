
def dobrar(numero):
    return numero * 2


resultado = dobrar(5)
print(f"O dobro de 5 é: {resultado}")


class Pessoa:
    def __init__(self, nome, idade):  
        self.nome = nome             
        self.idade = idade

    def apresentar(self):          
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."


p1 = Pessoa("Kaue", 20)


print(p1.apresentar())

