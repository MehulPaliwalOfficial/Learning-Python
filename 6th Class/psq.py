import math
from math import sqrt

input_number = int(input("Enter a number: "))
if input_number < 0:
    print("The square root of a negative number is not defined in the set of real numbers.")
else:
    result = sqrt(input_number)
    if result.is_integer():
        print(f"The square root of {input_number} is {int(result)}.")
    else:
        print(f"The square root of {input_number} is not a perfect square")