# Funcoes
def nome(parametro: str) -> str:
    print(parametro)

# Condicionais
valor = 5
if valor > 0:
    print("Positivo")
elif valor < 0:
    print("Negativo")
else:
    print("Nulo")

# True False

# Switch Case
# Não tem
caso = 5
if caso == 1:
    print("caso 1")
elif caso == 2:
    print("caso 2")
else:
    print("caso padrao")

# Estruturas de repeticao
#
# For
# Errado:
# for(i=0;i<10;i++)
#
# Certo:
for i in range(10):
    print(i)

# Por que é assim?
# O range retorna um objeto contendo uma sequencia de numeros,
# para saber mais acesse a documentacao do Python

# Outro exemplo:
# 1 a 10 de 2 em 2
for i in range(1, 10, 2):
    print(i)

# Percorrendo lista (item)
array = [1, 3, 5]
for i in array:
    print(i)

# Percorrendo lista (indice)
for i in range(len(array)):  # for i in range(3)
    print(i)

# Percorrendo string (str)
for i in "Curso Python":
    print(i)

# While
i = 0
while i < 10:
    i += 1
    print(i)

# Do While
# Também não tem ;-;
i = 0
while True:
    i += 1
    if i == 10:  # Condicaod de Parada
        break

## Entrada input()
nome = input('Digite seu nome: ')
print('Fala comigo, '+nome)
