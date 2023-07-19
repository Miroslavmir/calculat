def template_operation(_operation):
    if _operation == "+":
        return lambda _number1, _number2: f"{_number1} + {_number2} = {_number1 + _number2}"
    elif _operation == "*":
        return lambda _number1, _number2: f"{_number1} * {_number2} = {_number1 * _number2}"
    elif _operation == "-":
        return lambda _number1, _number2: f"{_number1} - {_number2} = {_number1 - _number2}"
    elif _operation == "/":
        return lambda _number1, _number2: f"{_number1} / {_number2} = {_number1 / _number2}"
    elif _operation == "%":
        return lambda _number1, _number2: f"{_number1} % {_number2} = {_number1 % _number2}"
    elif _operation == "**":
        return lambda _number1, _number2: f"{_number1} ** {_number2} = {_number1 ** _number2}"
    elif _operation == "//":
        return lambda _number1, _number2: f"{_number1} // {_number2} = {_number1 // _number2}"
    else:
        return None


operation = input("Enter operation(+, *, -, /, %, **, //): ")
func_calc = template_operation(operation)


number1 = int(input("Enter number1: "))
number2 = int(input("Enter number2: "))


result = func_calc(number1, number2)
print(result)
