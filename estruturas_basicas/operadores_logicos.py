saldo = 1000
saque = 200
limite = 100
curso = "Curso de Python"
nome_curso = curso
linguagens=["Java","Python","C++","C#","C"]
saques=[150,300,655,1500]

# Pergunta se saldo e maior ou igual a saque
# retorna true ou false
print(saldo >= saque)

# Mesmas condicoes anterioes porem adicionado
# o operador 'and' que funciona como && para mais uma condicao
print(saldo >= saque and saque <= limite)

# Operador logico 'or' ou.
print(saldo >= saque or saque <= limite)

# Operador de identidade
print(nome_curso is curso)
print(saldo is limite)

# Operadores de associacao
print("Python" in nome_curso)
print("python" in nome_curso)
print("C#" in linguagens)
print("20" in saques)