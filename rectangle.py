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

def prime_numbers(m):
    answer = []
    for j in range(2, m + 1):
        if is_prime(j) == True:
            answer.append(j)
    return answer

print(prime_numbers(20))

print("---------------------------------------")

def grades(my_list: list)-> str:
    """
    his function calculates maximum, minimum
    and mean value of the grades given 
    in my_list
    """
    