lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Pastel') # variavel composta
# Tuplas são imutáveis
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')#Aqui vai mostra a posição de onde esta cada elemento das tuplas/lista da variavel 

#faça comida para cada item em lanche | explicando o for | forma mais simples de se fazer
for comida in lanche:
    print(f'Eu vou comer {comida}')

for pos, comida in enumerate(lanche):# outra forma de fazer e ver a posição mas assim tem que usar duas variaveis
    print(f'Eu vou comer {comida} na posição {pos}')

print(sorted(lanche))# vai mostra o lanche em ordem, alfabetica/ mas deixa em lista []

print(len(lanche))