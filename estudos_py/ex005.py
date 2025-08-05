#cauculo da area de uma parede e mostra quantos litros vai precisar para pintar tudo

altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largarua da parede: '))

area = altura * largura

litros = area / 2

print(f'Sua parede é de {altura} X {largura} e a Área total da sua parede é: {area}, para pintar ela toda vai precisar de {litros} litros de tinta')