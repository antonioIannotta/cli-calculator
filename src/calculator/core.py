def sum(a: float, b: float) -> float:
    """
    This method adds two numbers together and returns the result.
    :param a: the first number
    :param b: the second number
    :return: the result
    """
    return a + b

def sub(a: float, b: float) -> float:
    """
    This method subtracts two numbers together and returns the result.
    :param a: the first number
    :param b: the second number
    :return: the result
    """
    return a - b

def mul(a: float, b: float) -> float:
    """
    This method multiplies two numbers together and returns the result.
    :param a: the first number
    :param b: the second number
    :return: the result
    """
    return a * b
def div(a: float, b: float) -> float:
    """
    This method divides two numbers together and returns the result.
    :param a: the first number
    :param b: the second number
    :return: the result
    """
    if b == 0:
        raise ZeroDivisionError
    return a / b