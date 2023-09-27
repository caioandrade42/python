# Array
import array as arr

# Criar um array de inteiros
array = arr.array('i', [1, 2, 3, 1])

# Acessar valor no array
print(array[1])

# Slice array
print(array[1:2])

# Procurar valor no array
print(array.index(1))

# Contar quantas vezes um valor apareceu
print(array.count(1))
