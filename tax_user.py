"""This script obtains the gross salary amount from user input and taxer.calculates the income tax to be paid on the salaary."""
import taxer  # import taxer module


gross = float(input("Enter gross salary in GHS:\t"))
net, tax = taxer.calculate(gross)
print(f"Total tax: GHS {tax:0.2f}")
print(f"Net salary: GHS {net:0.2f}")

while True:
    status = input("Would you like to compute tax on different gross salary?\t")
    if status in ["YES", "Yes", "yes", "Y", "y"]:
        gross = float(input("Enter gross salary in GHS:\t"))
        net, tax = taxer.calculate(gross)

        print(f"Total tax: GHS {tax:0.2f}")
        print(f"Net salary: GHS {net:0.2f}")
    else:
        print("Goodbye :)")
        break
