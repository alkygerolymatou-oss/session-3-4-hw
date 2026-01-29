try:
    gross = float(input("Enter gross salary: "))
    children = int(input("Enter number of children: "))


    if gross < 1000:
        tax_rate = 0.10
    elif gross < 2000:
        tax_rate = 0.12
    elif gross < 4000:
        tax_rate = 0.14
    else:
        tax_rate = 0.18


    if gross < 2000:
        tax_rate -= children * 0.01
    else:
        tax_rate -= children * 0.005


    if tax_rate < 0:
        tax_rate = 0

    net = gross * (1 - tax_rate)

    print("Net salary is:", net)

except ValueError:
    print("Please enter valid numbers.")
