import re

class Calculator:
    
    # Junior Developer Coding Test (Python)
    # CLI Calculator
    
    def calculate(self, s): # s means string
        result = 0
        current = 0
        sign = 1 # to handle sign // e.g. minus number (-1)
        stack = []
        for ss in s: # ss means substring
            if ss.isdigit():
                current = int(ss) + 10 * current # to prevent overflow
            elif ss in ["+", "-"]:
                result += sign * current
                current = 0
                if ss == "+":
                    sign = 1
                else: sign = -1
            elif ss == "(":
                stack.append(result)
                stack.append(sign)
                sign = 1
                result = 0
            elif ss == ")":
                result += current * sign
                result *= stack.pop()
                result += stack.pop()
                current = 0
            
        return result + current * sign

print("Welcome to our awesome calculator")
calc = Calculator()
user_input = ""
while user_input not in ["exit"]: # type exit to stop the loop
    regex = re.search('[a-zA-Z]', user_input) # to stripped out alphabet (only accept numbers)
    if regex != None:
        print("Please use numbers and basic operators.")
    user_input = input("-> ")
    feedback = "The answer is"
    output = calc.calculate(user_input)
    print(feedback, output)
print("Thank you for using our awesome calculator")
