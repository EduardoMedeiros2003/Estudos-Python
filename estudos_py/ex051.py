resp = 'S'
soma = cont = media = maior = menor = 0
while resp in 'Ss':
     n = int(input('Digite um número inteiro: '))
     soma += n
     cont += 1
     if cont == 1:
         maior = n
         menor = n
     else:
           if n > maior :
               maior = n
           if n < menor:
                menor = n
            
     resp = input('Deseja continuar ? [S/N]: ').upper().strip()[0]
media = soma / cont
print(f'Você digitou {cont} números e a soma dos números foi de : {soma} e a sua media foi de : {media:.2f} ')
print(f'O Maior número digitado foi de :{maior}, e o Menor número digitado foi de {menor}')
