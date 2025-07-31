#cauculo da area de uma parede e mostra quantos litros vai precisar para pintar tudo

altura = int(input('Digite a altura da parede: '))
largura = int(input('Digite a largarua da parede: '))

area = altura * largura

litros = area / 2

print(f'Área total da sua parede é: {area}, para pintar ela toda vai precisar de {litros} litros de tinta')