
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
            print("you have valid input")
            add_to_stack(response, stack)
        ##if input_operator?(response):
            ##attempt_calculation(response)
        ##if !valid_input?(response):
            ##print('Try typing a number or an operator.')

def valid_input(i):
    True if input_zero(i) or input_operator(i) or input_number(i) or 'q' or 'i' or 'p' or 'c' else False

def input_zero(i):
    True if i == '0' else False

def input_operator(i):
    True if i == '-' or i == '+' or i == '*' or i == '/' else False

def input_number(i):
    True if float(i) != 0 else False

def add_to_stack(i, stack):
    if input_zero(i):
        stack.append(i)
    if input_number(i):
        stack.append(float(i))
    return stack

def print_stack(stack):
    print('')
    print(stack)
    print('')

def farwell_message():
    print('goodbye')

if __name__ == '__main__': main()