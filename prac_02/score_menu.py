

# imports
# Here you could import any required modules, though for this script, no additional imports are needed.

# CONSTANTS
# If there were any constants needed in your script, they would be defined here.
MENU = """(G)et a valid score (must be 0-100 inclusive)
(P)rint result (copy or your function to determine the result from importscore.py)
(S)how stars (this should print as many stars as the score)
(Q)uit"""


def main():
    print(MENU)
    # 提示用户输入
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = float(input("Enter score: "))
            size_judgment(score)
        elif choice == "P":
            score_menu(score)
        elif choice == "S":
            star_print(score)
        else:
            print("Error, please enter the correct command")
        print(MENU)
        choice = input(">>> ").upper()
    print("Goodbye")

def size_judgment(input_str2):
    if input_str2 >= 0 and input_str2 <=100:
        pass
    else:
        print("Invalid score")


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

def star_print(input_str1):
    star = int(input_str1)
    print('*' * star)

main()
