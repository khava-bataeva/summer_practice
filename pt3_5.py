def not_prime(n):
    if n < 2:
        return True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return True
            return False


print([x for x in range(100) if not_prime(x)])
