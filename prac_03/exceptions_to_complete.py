"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""
is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True  # 如果输入成功，设置 is_finished 为 True，退出循环
    except ValueError:  # 捕获 ValueError 异常
        print("Please enter a valid integer.")
print("Valid result is:", result)