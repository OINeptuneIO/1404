usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45',
             'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
             'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

def main():
    user_input = input("Enter your username: ")
    if user_input in usernames:
        print("Access granted")
        process_numbers()
    else:
        print("Access denied")

def process_numbers():
    numbers = []
    for i in range(5):
        number = int(input("Number: "))  # Convert input to integer
        numbers.append(number)

    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    average = sum(numbers) / len(numbers)
    print(f"The average of the numbers is {average:.1f}")

main()