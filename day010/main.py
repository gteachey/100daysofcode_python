from art import logo


def calculate(n1, n2, sign):
    if sign == '+':
        result = n1 + n2
    elif sign == '-':
        result = n1 - n2
    elif sign == '/':
        result = n1 / n2
    elif sign == '*':
        result = n1 * n2
    else:
        result = "Invalid sign given"
    print(f"Answer is: {result}")


print(logo)
n1_value = float(input("Enter first value: "))
calc_sign = input("Enter calculation sign: ")
n2_value = float(input("Enter second value: "))

calculate(n1=n1_value, sign=calc_sign, n2=n2_value)
