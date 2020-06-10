#Desafio 007
print("\n Desafio 007")
number1=float(input('Insira a primeira nota:')) #Note que declaramos a nota como valor flutuante porque podem existir números quebrados
number2=float(input('Insira a segunda nota:'))
number=float((number1+number2)/2) #O cálculo de média aritmética consiste na somatória de todas as notas e depois o resultado é dividido pela quantidade de notas
print('A média aritmética das notas corresponde a {}'.format(number))