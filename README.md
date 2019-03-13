# Reverse Polish Notation (RPN) Calculator in Python

## Basic Info:
* Author: Tim Fielder
* Date: 03/13/19
* Version: 1.0
* Python Version: 3.7.1


## To run:
1. Go to https://github.com/tfielder/RPN_python_calculator.git.
2. From your command line (on a linux based-system) and the directory of your choice run `git clone https://github.com/tfielder/RPN_python_calculator.git`.
3. Change into the directory by running `cd RPN-Calculator`.
4. (Make sure you have a Python version installed).
5. Run `python RPN.py`.
6. Enjoy the calculator.

## Assumptions and Decisions:
This project assumes using the Python language and version 3+.
The program should notify the user if an invalid input is provided.
The program will notify the user if an attempt is made to divide by 0.
The program accepts positive float values or 0.
Email the author with any comments, suggestions, or bugs.

## Explanation:
In Reverse Polish Notation (RPN) the operators follow their operands; for instance, to add three and four one would write `3 4 +` rather then `3 + 4`.  If there are multiple operations, the operator is given immediately after its second operand; so the expression written `3 - 4 + 5` in conventional infix notation would be written `3 4 - 5 +` in RPN: first subtract 4 from 3, then add 5 to that.

Example: The infix expression `5 + ((1 + 2) * 4) - 3` can be written down like this in RPN: 5 1 2 + 4 * + 3 -

This calculator handles:

- At least 4 numbers

- The four basic arithmetic operations `+, -, *, /`.

- `standard in` and `standard out` to accept and return data.

- Entering `q` quits the application.

```
Sample:
1
2
+
= 3
2
*
= 6
4
-
= 2
q
goodbye
```
