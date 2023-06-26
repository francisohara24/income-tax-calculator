"""This script extracts the gross monthly salary amount from a csv file and calculates the income tax based on the extracted salary.
Each line of the csv file contains name and salary separated by commas.
Script outputs a new csv file comprising old csv file with income tax appended to each line.
"""
from taxer import calculate   # import tax calculator function

fh_input = open("data/salaries.csv", "r")  # open input file
fh_output = open("data/salaries_tax.csv", "w")  # open output file

for line in fh_input:
    line = line.strip()  # remove whitespace(newline character) at end of line
    name, salary = line.split(",")  # split line by comma and store results in variables name and salary.
    tax, net = calculate(float(salary))  # calculate tax and net income and store results in variables tax and net
    fh_output.write(name + "," + salary + ", " + str(tax) + ", " + str(net) + "\n")  # write results to output file

# close files
fh_input.close()
fh_output.close()
