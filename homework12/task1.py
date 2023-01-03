
class InputFormulaError(Exception):
    ...
    
class InputNumberError(Exception):
     ...
    
class InputOperatorError(Exception):
     ...
    


def add(a,b):
    return a+b

class Calculator:
    
    operators = ('+','-','*','/','**', '//')
    operation = {
        '+': lambda x, y: x+y,
        '-': lambda x, y: x-y,
        '*': lambda x, y: x*y,
        '**': lambda x, y: x**y,
        '/': lambda x, y: x/y,
        '//': lambda x, y: x//y,
    }
    
    def __init__(self) -> None:
        self.formula = None
    
    def validate_user_input(self, user_input: str):
        try:
            number_1, operator, number_2 = user_input.split(' ')
        except ValueError as e:
            raise InputFormulaError
        try:
            number_1, number_2 = int(number_1), int(number_2)
        except Exception as e:
            raise InputNumberError

        if operator not in self.operators:
            raise InputOperatorError
        
        return number_1, operator, number_2
            

    
if __name__ == '__main__':
     calc = Calculator()
     while True:
         user_input = input('Enter formula or "quit": ')
         if user_input == 'quit':
             print('Bye')
             break
         else:
             n_1, op, n_2 = calc.validate_user_input(user_input)
             try:
                 result = calc.operation[op](n_1, n_2)
             except ArithmeticError as err:
                 print(err)