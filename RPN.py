
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
    while response != 'q':
        response = input()
        if response == 'i':
            print_instructions()
        if response == 'c':
            print("you are clearing a stack")
        if response == 'p':
            print("you are printing the stack")
        ##if valid_input?(response):
            ##add_to_stack(response)
        ##if input_operator?(response):
            ##attempt_calculation(response)
        ##if !valid_input?(response):
            ##print('Try typing a number or an operator.')


def farwell_message():
    print('goodbye')

if __name__ == '__main__': main()