#Desafio 031
print("Desafio 031")
distance=float(input("Digite a distância da viagem em km:"))
if distance<200.0:
    price=distance*0.50
    print("O preçoda viagem para a distância de {}km equivale a R${}.".format(distance, price))
else: 
    price=distance*0.45
    print("O preço da viagem para a distância de {} equivale a R${}.".format(distance, price))