#Desafio 008
print("\n Desafio 008")
number=float(input('Insira o valor em metros:'))
number1=float(number*100) #Consideramos valor flutuante porque isso pode acontecer, e multiplicamos por 100 para encontrar os centímetros
number2=float(number*1000) #Para encontrar os milímetros é só multiplicarmos por 1000
print('O valor em centímetros corresponde a {}'.format(number1))
print('O valor em milímetros corresponde a {}'.format(number2))