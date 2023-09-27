# Formatar casas decimais
PI = 3.14159
print(f"Valor de PI: {PI:.2f}")
print(f"Valor de PI: {PI:.4f}")

# Formas diferentes de concatenacao
curso = "  Hello World        "

print(curso + "   .")
print(curso.strip() + ".")
print("+".join(curso.strip()))

# Alinhando textos
print("{:<30}".format("alinhado na esquerda"))
print("{:>30}".format("alinhado na direita"))
print("{:^30}".format("centralizado"))
print("{:#^30}".format("centralizado"))
print("Python".center(14, "#"))
print("Python".center(14))

# Alterando formato de apresentacao
# Sempre mostra o sinal
print("{:+f}; {:+f}".format(3.14, -3.14))

# Caso o numero for positivo, mostra com um espaço na frente
print("{: f}; {: f}".format(3.14, -3.14))

# Mostra o sinal apenas de for negativo (mesmo que {:f})
print("{:-f}; {:-f}".format(3.14, -3.14))

# Mostra o valor em bases diferentes
print("int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(42))
