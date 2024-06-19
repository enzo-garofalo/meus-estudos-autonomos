from model import CalculatorModel
from view import CalculatorView
from controller import CalculatorController

def main():
    model = CalculatorModel()
    view = CalculatorView()
    controller = CalculatorController(model, view)

    while True:
        print("\nOptions: add, subtract, multiply, divide, quit")
        operation = input("Enter operation: ").strip()
        
        if operation == 'quit':
            break
        
        try:
            a = float(input("Enter first number: ").strip())
            b = float(input("Enter second number: ").strip())
            controller.process(operation, a, b)
        except ValueError:
            view.display_error("Error: Invalid input")

if __name__ == "__main__":
    main()
