#Desafio 018
print("Desafio 018") #VERIFICAR, porque acho que o código está certo, mas não estou conseguindo resolver na calculadora
import math
angle=float(input("Insira o valor do ângulo:"))
seno=math.degrees(math.sin(angle))
cos=math.degrees(math.cos(angle))
tan=math.degrees(math.tan(angle))
print("O seno do ângulo {} vale {:.2f}, o cosseno vale {:.2f}, e a tangente vale {:.2f}.".format(angle,seno,cos,tan))