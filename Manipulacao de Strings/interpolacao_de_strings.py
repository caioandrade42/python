nome="Caio"
idade=28
profissao="Programador"
linguagem="Python"
dados={"nome":"Caio","idade":28,
       "linguagem":"Python","profissao":"Programador"}

print("Ola me chamo %s. Tenho %d anos de idade, trabalho como %s e estou matriculado "
      "no curso de %s"%(nome,idade,profissao,linguagem))
print("Ola me chamo {nome}. Tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado "
      "no curso de {linguagem}".format(linguagem=linguagem,profissao=profissao
                                       ,idade=idade,nome=nome))
print("Ola me chamo {nome}. Tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado "
      "no curso de {linguagem}".format(linguagem=linguagem,profissao=profissao
                                       ,idade=idade,nome=nome))
print(f"Ola me chamo {nome}. Tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado "
      f"no curso de {linguagem}.")

PI=3.14159
print(f"Valor de PI: {PI:.2f}")
print(f"Valor de PI: {PI:.4f}")

print("Ola me chamo {nome}. Tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado "
      "no curso de {linguagem}.".format(**dados))