def add(num1, num2):
    if type(num1) is not int and type(num1) is not float:
        return "Error: num1 must be a number"
    elif type(num2) is not int and type(num2) is not float:
        return "Error: num2 must be a number"
    else:
        return num1 + num2


test_cases = [
    {"num1": 1, "num2": 3, "expected": 4},
    {"num1": 1, "num2": "invalid", "expected": "Error: num2 must be a number"},
    {"num1": [1, 2, 3], "num2": 2, "expected": "Error: num1 must be a number"},
    {"num1": -1, "num2": 1, "expected": 0},
    {"num1": 3.5, "num2": 2.5, "expected": 6.0},
    {"num1": 100, "num2": 200, "expected": 300}
]

for test in test_cases:
    assert add(test["num1"], test["num2"]) == test["expected"]
    