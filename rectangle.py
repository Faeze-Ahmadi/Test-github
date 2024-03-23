def rectangle(a, b):
    """
    This function retuens erea 
    and perimeter of a rectangle
    """
    return a * b, 2 * (a + b)

print(rectangle(3,8))

def is_prime(n):
    if n == 1: 
        return False
    if n == 2: