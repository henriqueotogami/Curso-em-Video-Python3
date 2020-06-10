#Desafio 023
print("Desafio 023")
number=int(input("Insira um número de 0 a 9999:"))
unidade=number // 1 % 10
dezena=number // 10 % 10
centena=number // 100 % 10
milhar=number // 1000 % 10
print('Analisando o número {}'.format(number))
print("Unidade:{}".format(unidade))
print("Dezena: {}".format(dezena))
print("Centena:{}".format(centena))
print("Milhar: {}".format(milhar))