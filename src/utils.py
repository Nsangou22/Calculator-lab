def add(*args):
    """Return the sum of all numbers."""
    print("Add function executed")
    return sum(args)


def subtract(*args):
    """Subtract all following numbers from the first."""
    if not args:
        return 0
    result = args[0]
    for num in args[1:]:
        result -= num
    return result


def multiply(*args):
    """Multiply all given numbers."""
    result = 1
    for num in args:
        result *= num
    return result


def divide(*args):
    """Divide sequentially all given numbers."""
    if not args:
        return 0
    result = args[0]
    for num in args[1:]:
        if num == 0:
            raise ZeroDivisionError("It's dividable by Zero")
        result /= num
    return result

