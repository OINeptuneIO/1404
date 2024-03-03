"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator (not zero): "))  # Change this line
    if denominator == 0:  # Add this line to check if denominator is zero
        raise ZeroDivisionError("Denominator cannot be zero!")  # Raise ZeroDivisionError if denominator is zero
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError as error:  # Catch ZeroDivisionError into variable error
    print(error)  # Print error message
print("Finished.")