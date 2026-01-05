#Sempre que pensarmos em uma classe, temos que pensar quais são os atributos, ou seja, as características dessa entidade que queremos criar. Vamos supor que queremos criar uma entidade chamada pessoa, então precisamos pensar nas características de uma pessoa que queremos dentro de um sistema, como o RG e o CPF.
#Orientado a objetos vai precisar de class, vai ser sobre as caracteristicas de cada coisa para colocar os seus atributos
#Buscar abistração do mundo real para colocar no codigo, para os valores e atributos
#Sempre que temos esse __ significa que é um método especial que toda classe em Python possui
#self é a referência da instância que estamos usando no momento
#O __init__ é um metodo especial tal como o __str__ é um metodo especial para as class do python (objeto)
class Restaurante: 
    restaurantes = []
    def __init__(self, nome, categoria):   
        self._nome = nome.title()# Primeira letra maiuscula
        self._categoria = categoria.upper()# Todas as letras maiusculas
        self._ativo = False # O _ antes do nome do atributo faz uma proteção para ele, Não pode ser auterado
        Restaurante.restaurantes.append(self)

    def __str__(self):# vai mostra melhor no console como uma str
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{"Nome do Restaurante".ljust(25) } | {"Categoria".ljust(25) } | {"Status"}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo.ljust(25)}')

    @property # Vai modificar como o atributo vai ser lido
    def ativo(self):
        return '☑' if self._ativo else '☐'
    
    def alternar_estado(self):
        self._ativo = not self._ativo # O not inverte o valor


restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_praca.alternar_estado()
restalrante_pizza = Restaurante('Pizarele', 'Italiana')

verifica = restalrante_pizza.ativo
if verifica == False:
    print('O restaurante esta desativado!')
else:
    print('O restaurante esta ativado')

#O vars(é para ver em formato de dicionario)
Restaurante.listar_restaurantes()