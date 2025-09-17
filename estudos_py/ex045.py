
sexo = input('Digite seu sexo:[M/F]: ').strip().upper()[0]
while sexo not in 'MmFf':
    sexo = input('Invalido, porfavor Digite seu sexo:[M/F]: ').strip().upper()[0]
print(f'Seu sexo {sexo} foi registrado!')
