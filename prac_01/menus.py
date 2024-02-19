name = input("Enter name:")
while True:
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")
    choice = input("").lower()  # 将用户输入转换为小写，以便统一处理

    if choice == 'h':
        print("Hello", name)
    elif choice == 'g':
        print("Goodbye", name)
    elif choice == 'q':
        break  # 终止循环，退出程序
    else:
        print("Invalid choice")