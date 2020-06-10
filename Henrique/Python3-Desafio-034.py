#Desafio 034
print("Challenge 034")
salary=float(input("Please, insert your salary:"))
if salary>=1250.00:
    print("Your salary will be: R${}.".format(salary*1.10))
else:
    print("Your salary will be: R${}.".format(salary*1.15))