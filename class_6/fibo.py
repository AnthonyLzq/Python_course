# Recursividad

def fibo(n):
    if n > 1:
        return fibo(n-1) + fibo(n-2)
    elif n == 1 or n == 0:
        return 1

print(fibo(100))