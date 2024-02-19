"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

score = float(input("Enter score: "))
if score >= 0 and score <=100:
    if score >= 90:
        print("excellent")
    elif score >= 50:
        print("pass")
    else:
        print("bad")
else:
    print("Invalid score")