# Income Tax Calculator

# Variables
tax_rate = 0.20
gross = 0.0
dependents = 0
dep_deduction = 3000.0
flat_deduction = 10000.00
tax_deduction = 0.0
final_tax = 0.0

# Asking user for values
gross = float(input("Enter the gross income: "))
dependents = int(input("Enter the number of dependents: "))

# Computations
tax_deduction = (gross - flat_deduction) - (dependents * dep_deduction)
final_tax = tax_deduction * tax_rate

# Output results
print(f"The income tax is ${final_tax}")