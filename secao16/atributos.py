"""
POO - Atributos

Atributos -> representa as características do objeto. Ou seja, pelos atributos
nós conseguimos representar computacionalmente os estados de um objeto.

Em Python, dividimos os atributos em 3 grupos:
    - Atributos de instância;
    - Atributos de classe;
    - Atributos dinâmicos;

# Atributos de Instância
    São atributos declarados dentro do método construtor.

# OBS: Método construtor: É um método especial utilizado para a construção do
objeto.

# Em Java, um classe Lâmpada, incluindo seus atributos ficaria mais ou menos

public class Lampada() {
    private int voltagem;
    private String cor;
    private boolean ligada = false;

    public Lampada(int voltagem, String cor) {
        this.voltagem = voltagem;
        this.cor = cor;
    }
}

Em Python, por convenção, ficou estabelecido que, todo atributo de uma classe
é público. Ou seja, pode ser acessado em todo o projeto.
Caso queiramos demostrar que determinado atributo deve ser tratado como
privado, ou seja, que deve ser acessado/utilizado somente dentro da própria
classe onde está declarado, utiliza-se __ duplo underscore no ínicio de seu
nome.

Isso é conhecido também como Name Mangling.

# OBS: Lembre-se que isso é apenas uma convenção, ou seja, a linguagem Python
# não vai impedir que façamos acesso aos atributos sinalizados como privados
# fora da classe.

# Exemplo

user = Acesso('user@gmail.com', '123456')
print(user.email)
# print(user.__senha)  # AttributeError
print(user._Acesso__senha)  # temos acesso mas não deveriamos fazer esse acesso
# (Name Mangling)

print(user.mostra_senha())
print(user.mostra_email())

# O que significa atributos de instância?
# Significa, que ao criarmos instância/objetos de uma classe, todas as
# instâncias terão estes atributos.

user1 = Acesso('user1@gmail.com', '123456')
user2 = Acesso('user2@gmail.com', '654321')

print(user1.mostra_email())
print(user2.mostra_email())

# atributos de Classe
# são atributos, que são declarados diretamente na classe, ou seja, fora do
# construtor, geralmente já inicializamos um valor, e este valor é
# compartilhado entre todas as instâncias da classe. Ou seja, ao invés de cada
# instância ter seus próprios valores como é o caso dos atributos de instância
# com os atributos de classe todas as instâncias terão o mesmo valor para este
# atributo.

p1 = Produto('Playstation 4', 'Video Game', 2300)
p2 = Produto('Xbox S', 'Video Game', 4500)

print(p1.valor)
print(p2.valor)

# OBS: não precisamos criar uma instância de uma classe para fazer acesso a um
# atributo de classe

print(Produto.imposto)  # Acesso correto de um atributo de classe
print(p1.id)
print(p2.id)

# OBS: em linguagens como o Java, os atributos conhecidos como atributos de
# classe aqui em Python são chamados de atributos estáticos.
"""

# Classes com atributo de instância público


class Lampada:

    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False


class ContaCorrente:

    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Usuario:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


# atributos públicos e atributos privados


class Acesso:

    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    def mostra_senha(self):
        return self.__senha

    def mostra_email(self):
        return self.email

# Refatorar a Classe Produto

class Produto:

    # atributo de classe
    imposto = 1.05  # 0.05% de imposto
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id


# Atributos dinâmicos
# um atributos de instância que pode ser criado em tempo de execução.
# OBS: O atributo dinâmico será exclusivo da instância que o criou.

p1 = Produto('Playstation 4', 'Video Game', 2300)
p2 = Produto('Arroz', 'Mercearia', 5.99)

# criando um atributo dinâmico em tempo de execução

p2.peso = '5kg'  # Note que na classe Produto não existe o atributo peso
print(f'Produto: {p2.nome}, Descrição: {p2.descricao}, Valor: {p2.valor}, Peso: {p2.peso}')
# print(f'Produto: {p1.nome}, Descrição: {p1.descricao}, Valor: {p1.valor}, Peso: {p1.peso}')

# Deletando atributos
print(p1.__dict__)
print(p2.__dict__)

del p2.peso
del p2.valor
del p2.descricao

print(p1.__dict__)
print(p2.__dict__)
