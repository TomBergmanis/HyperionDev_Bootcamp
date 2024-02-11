# write a program with two compilation errors, a runtime error and a logical error
# next to each error add a comment tha texplains what type of error is is and why it occurs. 

print("========= How NOT to calculate the area of a square! ===========")

1_length = 10 # Compilation error 1: incorrect variable name. Variables cannot start with a number.
        width = 10 # Compliation error 2: indent not needed. Indentation does not match the indentaion of the former statement. indentaion must be consistent in Python

incorrect_area = length ** width # logical error: not how you calculate the area of a square. This is the wrong formula to calculate the area of a square. The correct way is length * width

print("Incorrect area: " + str(incorrect_area)) 

num1 = 12
num2 = 0

calc = num1 / num2 # RunTimeError: (ZeroDivisionError) as you cant divide a number by zero/ dividing anumber by 0 in python results in undefined output. 