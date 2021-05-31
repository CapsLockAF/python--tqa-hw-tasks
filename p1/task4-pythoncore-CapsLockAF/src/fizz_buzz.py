def fizz_buzz(param):
    #Type your code here
    # if param % 3 == 0 and param % 5 == 0:
    #     return "FizzBuzz"
    # elif param % 3 == 0:
    #     return "Fizz"
    # elif param % 5 == 0:
    #     return "Buzz"
    #
    # elif param % 3 != 0 or param % 5 != 0:
    #     return str(param)
    return param % 5 == 0 and param % 3 == 0 and "FizzBuzz" or \
           param % 3 == 0 and "Fizz" or \
           param % 5 == 0 and "Buzz" or \
           str(param)
