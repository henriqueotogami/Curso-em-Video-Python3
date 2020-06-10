#Desafio 015
print("\n Desafio 015")
days=int(input("informe quantos dias serão alugados:"))
dist=float(input("Informe a distância percorrida (km):"))
price=(dist*0.15)+(days*60)
print("O preço a pagar pelos {} dias, na distância de {}km, equivale a R${:.2f}".format(days, dist, price))