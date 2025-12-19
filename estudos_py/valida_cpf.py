def valida_cpf(cpf):
    # Remove espaços
    cpf = cpf.strip()

    # Verifica se tem só números
    if not cpf.isdigit():
        return 'Erro: O CPF deve conter apenas números!'

    # Verifica tamanho
    if len(cpf) != 11:
        return 'Erro: O CPF deve conter exatamente 11 dígitos!'

    # Elimina CPFs inválidos conhecidos
    if cpf == cpf[0] * 11:
        return 'Erro: CPF inválido!'

    # 🔹 Cálculo do primeiro dígito
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)

    digito1 = (soma * 10) % 11
    if digito1 == 10:
        digito1 = 0

    # 🔹 Cálculo do segundo dígito
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)

    digito2 = (soma * 10) % 11
    if digito2 == 10:
        digito2 = 0

    # 🔹 Verificação final
    if digito1 == int(cpf[9]) and digito2 == int(cpf[10]):
        return 'CPF válido.'
    else:
        return 'CPF inválido.'


cpf = input('Digite seu CPF: ')
print(valida_cpf(cpf))
