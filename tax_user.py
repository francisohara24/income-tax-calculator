"""This script obtains the gross salary amount from user input and calculates the income tax to be paid on the salaary."""
from taxer import calculate  # import taxer function


gross = float(input("Enter gross salary in GHS:\t"))
net_amount, tax_amount = calculate(gross)
print(f"Total tax: GHS {tax_amount:0.2f}")
print(f"Net salary: GHS {net_amount:0.2f}")

while True:
    status = input("Would you like to compute tax on different gross salary?\t")
    if status in ["YES", "Yes", "yes", "Y", "y"]:
        gross = float(input("Enter gross salary in GHS:\t"))
        net_amount, tax_amount = calculate(gross)

        print(f"Total tax: GHS {tax_amount:0.2f}")
        print(f"Net salary: GHS {net_amount:0.2f}")
    else:
        print("Goodbye :)")
        break
