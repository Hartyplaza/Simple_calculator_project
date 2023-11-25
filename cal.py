def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def division(a, b):
    return a / b


cal_dict = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": division
}


def calculator():
    number_1 = int(input("Enter first number: "))
    for symbols in cal_dict:
        print(symbols)

    continue_flag = True
    while continue_flag:
        operator = input("Pick an operator: ")
        number_2 = int(input("Enter second number: "))
        cal_func = cal_dict[operator]
        output = cal_func(number_1, number_2)
        print(f"{number_1} {operator} {number_2} = {output}")

        calculate_again = input("""
Enter 'y' to continue calculation from {output}
Enter 'n' to start fresh calculation 
Enter 'x' to Exit: """).lower()

        if calculate_again == 'y':
            number_1 = output

        elif calculate_again == 'n':
            continue_flag = False
            calculator()

        else:
            continue_flag = False
            print("bye")


calculator()

