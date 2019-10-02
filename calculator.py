from arithmetic import *


# Your code goes here
def calculator():
    result = None
    try:
        while True:
            user_input = input("What would you like to calculate? ").split()

            num1 = int(user_input[1])

            if num1 == 'cube' or num1 != 'pow':
                num2 = None

            else:
                num2 = int(user_input[2])


            if user_input[0] == 'q':
                return

            elif user_input[0] == '+':
                result = add(num1, num2)

            elif user_input[0] == '-':
                result = substract(num1, num2)
                    
            elif user_input[0] == '*':
                result = multiply(num1, num2)

            elif user_input[0] == '/':
                result = divide(num1, num2)

            elif user_input[0] == 'square':
                result = square(num1)

            elif user_input[0] == 'cube':
                result = cube(num1)

            elif user_input[0] == 'pow':
                result = power(num1, num2) 

            elif user_input[0] == 'mod':
                result = mod(num1, num2)
                

            print(result)            

    except ValueError:
            print("Invalid argument type")

calculator()