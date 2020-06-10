#Desafio 033
print("Desafio 033")
number1=int(input("Please insert the firts number:"))
number2=int(input("Now, insert the second number:"))
number3=int(input("Finally, insert the third number:"))
if number1>number2:
    if number1>number3:
        print("The first number is the bigger than others number.")
else:
    if number2>number3:
        print("The second number is the bigger than others.")
    else:
        print("The third number is the bigger than others.")