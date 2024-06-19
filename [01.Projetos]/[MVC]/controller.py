from model import CalculatorModel
from view import CalculatorView

class CalculatorController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def process(self, operation, a, b):
        if operation == 'add':
            result = self.model.add(a, b)
            self.view.display_result(result)
       
        elif operation == 'subtract':
            result = self.model.subtract(a, b)
            self.view.display_result(result)
       
        elif operation == 'multiply':
            result = self.model.multiply(a, b)
            self.view.display_result(result)
        
        elif operation == 'divide':
            result = self.model.divide(a, b)
            if result == "Division by zero":
                self.view.display_error(result)
            else:
                self.view.display_result(result)
        
        else:
            self.view.display_error(" Unknown operation")
