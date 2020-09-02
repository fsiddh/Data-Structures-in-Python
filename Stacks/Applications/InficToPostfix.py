# Program to convert infix expression to postfix expression
 
# method that returns the priority of the operator
def priority(operator):
    if operator == '+' or operator == '-':
        return 1
 
    elif operator == '*' or operator == '/' or operator == '%':
        return 2
 
    elif operator == '^':
        return 3
 
    else:
        return 0
 
# method that converts string in infix to postfix
# all the strings are assumed to be valid expressions
def in2postfix(infixString):
    # taking a list variable to store operators
    stack = []
 
    # result string variable
    postfixString = ""
    i = 0
 
    # loop till i is in the range of the length of string
    while i in range(0, len(infixString)):
 
        # if an alphabet is found then copy it to the output string
        if infixString[i].isalpha():
            postfixString += infixString[i]
 
 
        # if an opening bracket is found then put it in stack
        elif infixString[i] == '(' or infixString[i] == '[' or infixString[i] == '{':
            stack.append(infixString[i])
 
 
        # if an closing bracket is found then
        # keep removing the operators from the stack and add them to postfix string until you find the corresponding opening bracket
        elif infixString[i] == ')' or infixString[i] == ']' or infixString[i] == '}':
 
            if infixString[i] == ')':
                while stack[-1] != '(':
                    postfixString += stack.pop()
                stack.pop()
 
            if infixString[i] == ']':
                while stack[-1] != '[':
                    postfixString += stack.pop()
                stack.pop()
 
            if infixString[i] == '}':
                while stack[-1] != '{':
                    postfixString += stack.pop()
                stack.pop()
 
        # if none of the above cases are satisfied then we surely have an operator
        else:
 
            # if the stack if empty then we simply put the operator in stack
            if len(stack) == 0:
                stack.append(infixString[i])
 
            # if not then we compare the priority of the stack top and current operator
            else:
 
                # if the priority of current operator if high then push it onto the stack
                if priority(infixString[i]) > priority(stack[-1]):
                    stack.extend(infixString[i])
 
 
                # if the priority of current operator is less than or equal to the stack top then
                # pop the stack top and add it to the postfix string
                elif priority(infixString[i]) <= priority(stack[-1]):
                    postfixString += stack.pop()
                    position = len(stack) - 1
 
                    # now if you have an operator that has equal priority as of current operator then pop
                    while position >= 0 and priority(stack[position]) == priority(infixString[i]):
                        postfixString += stack.pop()
                        position -= 1
                        if position < 0:
                            break
 
                    stack.extend(infixString[i])
 
        # increment the value of i
        i += 1
 
    # at the end remove all the operators from the stack
    while len(stack) != 0:
        postfixString += stack.pop()
       
    # return the result
    return postfixString
 
# main function
infix = input("Enter the Infix Expression : ")
postfix = in2postfix(infix)
print("The converted Expression in Postfix is : " + postfix)