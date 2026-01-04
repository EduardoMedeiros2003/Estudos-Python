#Sempre que pensarmos em uma classe, temos que pensar quais são os atributos, ou seja, as características dessa entidade que queremos criar. Vamos supor que queremos criar uma entidade chamada pessoa, então precisamos pensar nas características de uma pessoa que queremos dentro de um sistema, como o RG e o CPF.
#Orientado a objetos vai precisar de class, vai ser sobre as caracteristicas de cada coisa para colocar os seus atributos
#Buscar abistração do mundo real para colocar no codigo, para os valores e atributos
#Sempre que temos esse __ significa que é um método especial que toda classe em Python possui
#self é a referência da instância que estamos usando no momento
#O __init__ é um metodo especial tal como o __str__ é um metodo especial para as class do python (objeto)
class Restaurante: 
    restaurantes = []
    def __init__(self, nome, categoria):   
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):# vai mostra melhor no console como uma str
        return f'{self.nome} | {self.categoria}'
    
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')


restaurante_praca = Restaurante('Praça', 'Gourmet')

restalrante_pizza = Restaurante('Pizarele', 'Italiana')

restalrante_pizza.ativo= True


verifica = restalrante_pizza.ativo
if verifica == False:
    print('O restaurante esta desativado!')
else:
    print('O restaurante esta ativado')

#O vars(é para ver em formato de dicionario)
Restaurante.listar_restaurantes()