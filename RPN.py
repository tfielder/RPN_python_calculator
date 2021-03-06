
def main():
    welcome_message()
    print_instructions()
    run_calculator()
    farewell_message()

def welcome_message():
    print('')
    print('Welcome to the Reverse Polish Notation Calculator')

def print_instructions():
    print('')
    print("At anytime type 'q' to quit the program, 'i' for a list of instructions.")
    print("This calculator is based on Reverse Polish Notation (RPN)")
    print("where the operators follow their operands.")
    print("Type in a value and press enter to push a value to the stack.")
    print("Type in an operator '+', '-', '/', or '*' with two or more values")
    print("in the stack to conduct an operation.")
    print("To empty the stack or calculator, type 'c'.")
    print("To print the current stack, type 'p'.")

def run_calculator():
    response = ''
    stack = []
    while response != 'q':
        response = input()
        if response == 'i':
            print_instructions()
        if response == 'c':
            stack.clear()
        if response == 'p':
            print_stack(stack)
        if valid_input(response):
            add_to_stack(response, stack)
        if input_operator(response):
            attempt_calculation(response, stack)
        if valid_input(response) == False:
            print('Try typing a number or an operator.')

def valid_input(i):
    if input_number(i) or input_operator(i):
        return True
    elif i == "q" or i == "i" or i == "p" or i == "c":
        return True
    else:
        return False

def input_operator(i):
    if i == '-' or i == '+' or i == '*' or i == '/':
        return True
    else:
        return False

def input_number(i):
    try:
        float(i)
        return True
    except:
        return False

def add_to_stack(i, stack):
    if input_number(i):
        stack.append(float(i))

def attempt_calculation(operator, stack):
    if enough_operands(stack) == False:
        print("Check your notation, there are not enough elements to calculate")
    if division_by_zero(operator, stack) == True:
        print('Cannot divide by zero')
    if valid_calculation(operator, stack) == False:
        return
    calculate(operator, stack)

def enough_operands(stack):
    if len(stack) >= 2:
        return True
    else:
        return False

def division_by_zero(operator, stack):
    if stack[-1] == 0 and operator == '/':
        return True
    else:
        return False

def valid_calculation(operator, stack):
    if enough_operands(stack) and division_by_zero(operator, stack) == False:
        return True
    else:
        return False

def calculate(operator, stack):
    determine_calculation(operator, stack)
    update_stack(stack)
    print_result(stack)

def determine_calculation(operator, stack):
    if operator == '+':
        stack[-2] = stack[-2] + stack[-1]
    if operator == '-':
        stack[-2] = stack[-2] - stack[-1]
    if operator == '*':
        stack[-2] = stack[-2] * stack[-1]
    if operator == '/':
        stack[-2] = stack[-2] / stack[-1]

def update_stack(stack):
    stack.pop()
    if stack[-1] % 1 == 0:
        stack[-1] = int(stack[-1])

def print_result(stack):
    print("=" + str(stack[-1]))

def print_stack(stack):
    print('')
    print(stack)
    print('')

def farewell_message():
    print('goodbye')

if __name__ == '__main__': main()