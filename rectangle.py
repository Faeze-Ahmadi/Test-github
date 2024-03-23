def rectangle(a, b):
    """
    This function retuens erea 
    and perimeter of a rectangle
    """
    return a * b, 2 * (a + b)

print(rectangle(3,8))

print("---------------------------------------")

def is_prime(n):
    if n == 1: 
        return False
    if n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False 
    return True

print(is_prime(101))