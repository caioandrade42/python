nome = "Caio"
idade = 28
profissao = "Programador"
linguagem = "Python"

dados = {"nome": "Caio", "idade": 28,
         "linguagem": "Python", "profissao": "Programador"}

print("1 - Ola me chamo %s. Tenho %d anos de idade, trabalho como %s e estou matriculado "
      "no curso de %s" % (nome, idade, profissao, linguagem))
print("2 - Ola me chamo {nome}. Tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado "
      "no curso de {linguagem}".format(linguagem=linguagem, profissao=profissao, idade=idade, nome=nome))
print("3 - Ola me chamo {}. Tenho {} anos de idade, trabalho como {} e estou matriculado "
      "no curso de {}".format(nome, idade, profissao, linguagem))
print(f"4 - Ola me chamo {nome}. Tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado "
      f"no curso de {linguagem}.")
print("5 - Ola me chamo {nome}. Tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado "
      "no curso de {linguagem}.".format(**dados))

