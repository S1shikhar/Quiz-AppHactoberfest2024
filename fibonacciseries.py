def fibonacci(n, memo={}):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n in memo:
        return memo[n]
    else:
        memo[n] = fibonacci(n-2) + fibonacci(n-2)
        return memo[n]

# Driver Program
print(fibonacci(9))
