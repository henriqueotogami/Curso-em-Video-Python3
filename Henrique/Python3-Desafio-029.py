#Desafio 029
print("Desafio 029")
velocidade=float(input("Digite a velocidade do carro:"))
if velocidade > 80.0:
    multa=(velocidade-80.0)*7
    print("O valor da multa corresponde a R${:.2f}, para a velocidade {}km/h acima do limite permitido.".format(multa,(velocidade-80.0)))
else: print("A velocidade inserida está dentro do limite permitido. Não há multa.")