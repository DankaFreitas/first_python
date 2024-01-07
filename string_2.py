nome = "carlos"
idade = 31
profissao = "Programador"
linguagem = "Python"

saldo = 14.444

dados = {"nome": "Oberdã" , "idade" : 31}

print("\n=======================================================================")
print("old style\n")
print("Nome: %s \nIdade: %d" % (nome, idade))
print("=======================================================================")

print("metodo format \n")
print("Nome: {} \nIdade: {}" .format(nome,idade))
print("=======================================================================")

print("metodo format 2 \n")
print("Nome: {0} \nIdade: {1}{1}" .format(nome,idade))
print("=======================================================================")

print("metodo format 3 \n")
print("Nome: {name} \nIdade: {age}" .format(name=nome, age=idade))
print("=======================================================================")

print("metodo format 4 \n")
print("Nome: {nome} \nIdade: {idade}" .format(**dados))
print("=======================================================================")

print(" f - string \n")
print(f"Nome: {nome} \nIdade: {idade}")
print("=======================================================================")

print(" f - string \n")
print(f"Nome: {nome} \nIdade: {idade} \nSaldo: {saldo:10.2f}")
print("=======================================================================")