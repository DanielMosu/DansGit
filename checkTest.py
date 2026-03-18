"""
    Test function to print a star pattern.
    The pattern is a pyramid of stars, where the number of stars increases by 2 for each level.
    The user is prompted to enter the number of levels for the pyramid.
    Additionally, the code includes a print statement to display a directory name, which is not related to the star pattern."""
num = int(input("Enter number: "))
for start in range(1, num+1):
    spaces = num - start
    stars = 2 * start - 1
    print(" " * spaces + "*" * stars)
