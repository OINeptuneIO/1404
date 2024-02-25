"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random

def main():
    """判断分数"""
    score = float(input("Enter score: "))
    score_menu(score)
    random_score = random.randint(0, 100)
    score_menu(random_score)


def score_menu(input_str):
    """具体细节"""
    if input_str >= 0 and input_str <=100:
        if input_str >= 90:
            print("excellent")
        elif input_str >= 50:
            print("pass")
        else:
            print("bad")
    else:
        print("Invalid score")

main()




