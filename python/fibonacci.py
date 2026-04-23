# fibonacci sequence
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

# Calling the function
fibonacci(10)