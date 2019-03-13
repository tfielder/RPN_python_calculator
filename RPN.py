
def main():
    welcome_message()
    print_instructions()
    run_calculator()
    farwell_message()

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
            print("you are clearing a stack")
        if response == 'p':
            print_stack(stack)
        if valid_input(response):
            add_to_stack(response, stack)
        if input_operator(response):
            attempt_calculation(response)
        if valid_input(response) == False:
            print('Try typing a number or an operator.')

def valid_input(i):
    if input_number(i) or input_operator(i) or input_number(i):
        return True
    elif i == "q" or i == "i" or i == "p" or i == "c":
        return True
    else:
        return False

def input_zero(i):
    if i == '0':
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
    if input_zero(i):
        stack.append(i)
    if input_number(i):
        stack.append(float(i))

def attempt_calculation(operator):
    #if enough_operands:
    #    print("Check your notation, there are not enough elements to calculate")
    #if division_by_zero:
    #   print('Cannot divide by zero')
    #if valid_calculation == False:
    #    return
    #calculate(operator)
    print('attempt calculation')

def print_stack(stack):
    print('')
    print(stack)
    print('')

def farwell_message():
    print('goodbye')

if __name__ == '__main__': main()