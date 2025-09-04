# um número primo so é divisivel 2 vezez, se paddar disso não é primo
numero = int(input('Digite um número para verificar se é primo ou não: '))
tot = 0
for c in range(1, numero +1):
   if numero % c == 0:
      print('\033[33m', end='')
      tot += 1
   else:
      print('\033[31m', end='')
   print(c, end=' ')

print(f'\n\033[mO número {numero} foi divisível {tot} vezes')
if tot ==2:
   print('O número é primo!!')
elif tot != 2:
   print('O número NÃO é primo!!')
print('Fim')
