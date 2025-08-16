import math
#Algoritimo para descoobre seno, cosseno e tangente de um ângulo
angulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(angulo)) #Trasforma em angulo o número
print(f'O ângulo de {angulo} tem o SENO de {seno:.2f}')
cosseno = math.cos(math.radians(angulo))
print(f'O ângulo de {angulo} tem o COSSENO de {cosseno:.2f}')
tangente = math.tan(math.radians(angulo))
print(f'O ângulo de {angulo} tem a TANGENTE de {tangente:.2f}')