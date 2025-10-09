expressao = input('Digite uma expressão matemática: ')
pilha = []

for simb in expressao:
    if simb == '(':
        pilha.append('(')# Adiciona um ( a pilha 
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()# remove o último elemento
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Expressão válida ✅')
else:
    print('Expressão inválida ❌')
