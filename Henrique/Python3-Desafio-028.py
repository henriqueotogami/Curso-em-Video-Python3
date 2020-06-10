#Desafio 028
print("Desafio 028")
import random
print("O computador vai sortear um número inteiro de 0 a 5.")
think=random.randint(0,5)
print("O número foi sorteado.")
digit=int(input("Tente descobrir qual número é esse.\n Insira um número a seguir, entre 0 e 5:"))
if think == digit:
    print("O compotador sorteou o número {}. Você acertou!".format(think))
else: print("O computador sorteu o número {}. Que pena! Você errou. \nTente novamente.".format(think))