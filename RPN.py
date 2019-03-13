
def main():
    welcome_message()
    print_instructions()
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

def farwell_message():
    print('goodbye')

if __name__ == '__main__': main()