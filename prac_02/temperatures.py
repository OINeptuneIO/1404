"""Pseudocode for temperature conversion"""

# imports
# Here you could import any required modules, though for this script, no additional imports are needed.

# CONSTANTS
MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    """编排温度转换的主要函数。"""
    print(MENU)
        # 提示用户输入
    choice = input(">>> ").upper()
    while choice != "Q":
        chooice_menu(choice)
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def chooice_menu(input_str):
    """验证输入字符串的长度并打印星号或引发ValueError。"""
    if input_str == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius * 9.0 / 5 + 32
        print(f"Result: {fahrenheit:.2f} F")
    elif input_str == "F":
        # TODO: Write this section to convert F to C and display the result
        # Hint: celsius = 5 / 9 * (fahrenheit - 32)
        # Remove the "pass" statement when you are done. It's a placeholder.
        fahrenheit = float(input("fahrenheit: "))
        celsius = 5 / 9 * (fahrenheit - 32)
        print(f"Result: {celsius:.2f} C")
    else:
        print("Invalid option")
        
main()