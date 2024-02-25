"""Module docstring: This script prompts the user for input and prints a number of asterisks based on the input length."""

# imports
# Here you could import any required modules, though for this script, no additional imports are needed.

# CONSTANTS
# If there were any constants needed in your script, they would be defined here.


def main():
    """编排输入验证和打印星号动作的主要函数。"""
    try:
        # 提示用户输入
        user_input = input("please enter your password:")

        # 验证输入长度并作出相应的响应
        print_star(user_input)
    except ValueError as e:
        print(e)

def print_star(input_str):
    """选择菜单"""
    if len(input_str) < 6:
        raise ValueError("Error: Fewer than 6 characters entered.")
    else:
        print("*" * len(input_str))

main()