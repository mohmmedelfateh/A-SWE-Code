# Single Responsibility Principle
class Calculator:
    def sum(self, a, b):
        return a + b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b


class DivisionErrorChecker:
    @staticmethod
    def check_division_error(b):
        if b == 0:
            raise ValueError("Cannot divide by zero")


class ResultSaver:
    def save(self, result):
        print("Saved result to database")


if __name__ == "__main__":
    calculator = Calculator()
    result_saver = ResultSaver()
    division_error_checker = DivisionErrorChecker()

    a = int(input('Enter The Numerator: '))
    b = int(input('Enter The Denominator: '))

    try:
        division_error_checker.check_division_error(b)
        result = calculator.divide(a, b)
        print("Result of division:", result)  # Print the result of division
        result_saver.save(result)
    except ValueError as e:
        print(e)
