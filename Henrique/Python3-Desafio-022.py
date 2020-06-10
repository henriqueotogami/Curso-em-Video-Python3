#Desafio 022
print("Desafio 022")
nome=str(input("Digite o seu nome:"))
print("O seu nome em letras maiúsculas: {}\n O seu nome em letras minúsculas:{}".format(nome.upper(), nome.lower()))
print("O seu nome tem ao todo {} letras.".format(len(nome)-nome.count(' ')))
nome1=nome.split()
print("O seu primeiro nome:{}.".format(nome1[0]))
print("O seu primeiro nome tem {} letras.".format(len(nome1[0])))