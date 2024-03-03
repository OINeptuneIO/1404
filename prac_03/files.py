# Write code that asks the user for their name,
# then opens a file called "name.txt" and writes that name to it.
# Remember to close your file.

name = input("Enter your name: ")

with open('name.txt', 'w+') as file:  # 使用 'w+' 模式
    file.write(name + '\n')

# Write code that opens "name.txt" and reads the name (as above),
# then prints, "Your name is Bob" (or whatever the name is in the file).

with open('name.txt', 'r') as file:
    name = file.read().strip()  # 去除末尾的换行符
    print(f"Your name is {name}")

# Create a text file called "numbers.txt", save it in your prac directory.
# Put the following three numbers on separate lines in the file and save it:
# 17
# 42
# 400

# Write code that opens "numbers.txt", reads only the first two numbers,
# adds them together then prints the result, which should be... 59.

with open('numbers.txt', 'w+') as file:  # 使用 'w+' 模式
    file.write('17\n42\n400\n')

with open('numbers.txt', 'r') as file:
    number1 = int(file.readline())
    number2 = int(file.readline())
    total = number1 + number2
    print(total)

# Now write a fourth block of code that prints the total for all lines in "numbers.txt"
# or a file with any number of numbers.


total = 0
with open('numbers.txt', 'r') as file:
    for line in file:
        number = int(line)
        total += number
print(total)