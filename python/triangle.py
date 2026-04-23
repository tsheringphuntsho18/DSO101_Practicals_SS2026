# triangle with for loops
n = 6
for i in range(1, n + 1):
    print("*" * i)
print('')

# triangle with centered alignment
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
print('')

# inverted triangle with for loops
for i in range(n, 0, -1):
    print("*" * i)
print('')

# triangle with while loops
i = 1
while i <= n:
    print("*" * i)
    i += 1

