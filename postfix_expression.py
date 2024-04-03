class postfix_expression_evaluation :
    def __init__(self):
        self.stack = []
    ##
    def evaluate_postfix(self,postfix):
        for char in postfix:
            if char.isdigit():
                self.stack.append(int(char))
            else:
                self.operand2 = self.stack.pop()
                self.operand1 = self.stack.pop() 
                if char == '+':
                    self.stack.append(self.operand1 + self.operand2)
                elif char == '-':
                    self.stack.append(self.operand1 - self.operand2)
                elif char == '*':
                    self.stack.append(self.operand1 * self.operand2)
                elif char == '/':
                    self.stack.append(self.operand1 // self.operand2)
                    
        return self.stack[0]
##
if __name__=='__main__':
    postfix_expression = input("Enter postfix expression: ")
    obj_postfix_expression_evaluation = postfix_expression_evaluation()
    result = obj_postfix_expression_evaluation.evaluate_postfix(postfix_expression)
    print("Result:", result)
##