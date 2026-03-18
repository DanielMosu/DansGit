num = int(input("Enter number: "))

for start in range(1, num+1):
    spaces = num - start
    stars = 2 * start - 1
    print(" " * spaces + "*" * stars)