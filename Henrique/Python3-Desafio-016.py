#Aula 08 - 01/02/2020 - Utilizando módulos
import math #importa a biblioteca inteira de matemática
number=int(input("Digite um número:")) 
raiz=math.sqrt(number) #realiza a raíz quadrada no número digitado no terminal
print("A raíz quadrada de {} é igual a {:.2f}".format(number,math.ceil(raiz))) #Imprime na tela o valor arredondado para cima
print("A raíz quadrada de {} é igual a {:.2f}".format(number,math.floor(raiz))) #Imprime na tela o valor arredondado para baixo

#Desafio 016
print("\n Desafio 016")
number=float(input("Digite um número:"))
number=int(number)
print("A parte inteira do número corresponde a {}".format(number))