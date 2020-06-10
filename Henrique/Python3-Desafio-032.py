#Desafio 032
print("Desafio 032")
year=int(input("Digite um ano:"))
import calendar
if calendar.isleap(year):
    print("Esse ano é bissexto")
else: print("Esse ano não é bissexto.")