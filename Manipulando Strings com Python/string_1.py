print("=======================================================================")
print("MAIUSCULO, MINUSCULO E TITULO\n")

nome ="oBeRdã"

print(nome.upper())
print(nome.lower())
print(nome.title())
print("=======================================================================")

print("ESPACAMENTO\n")
texto = "  Hello!  "

print(texto + ".")
print(texto.strip() + ".")
print(texto.rstrip() + ".")
print(texto.lstrip() + ".")

print("=======================================================================")


print("JUNCAO E CENTRALIZACAO\n")

menu = "Python"

print("###" + menu + "###")
print(menu.center(14))
print(menu.center(14, "#"))
print("-".join(menu))