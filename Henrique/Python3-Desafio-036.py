# Challenge 036 - 04/21/2021 - Henrique Matheus Alves Pereira
# Write a program to approve the bank loan for the purchase of a home.
# Ask the price of the house, the buyer's salary and how many years he will pay.
# The monthly installment cannot exceed 30% of the salary or the loan will be denied.
print("Challenge 036")
print("Please, for the following information, enter only two digits after the comma.")
priceHouse = float(input("1 - Please, enter the purchase price of the home (R$):"))
financingTime = float(input("2 - Please, enter the financing time of the home (Years):"))
salary = float(input("3 - Please, enter you salary (R$):"))
bankLoanReleased = "Bank loan released, considering that the monthly installment is below 30% of the informed salary."
bankLoanNotReleased = "Bank loan not released, considering that the monthly installment amount is above 30% of the informed salary."
monthlyInstallment = float(priceHouse/(financingTime*12))
print("The monthly installment is: R${:.2f}" .format(monthlyInstallment))
print(bankLoanReleased) if monthlyInstallment <= float(salary*0.3) else print(bankLoanNotReleased)
print("Financial institutions accept to commit up to 30% of the gross family income in real estate financing. Source: https://ka.com.br/qual-e-a-renda-para-financiamento-com-a-caixa/")