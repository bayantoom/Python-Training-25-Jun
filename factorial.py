# The first function `factorial(n: int) -> int` should return the factorial of the number n. 
# The second function `list_factorial([n1, n2, n3, ...]) -> List[int]` should return a list of factorials of the numbers in the input list.

def factorial(n: int) -> int:
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def list_factorial(*args) -> list[int]:
    my_list = []
    for arg in args:
       fac = factorial(arg)
       my_list.append(fac)

    return my_list