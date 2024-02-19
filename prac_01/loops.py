for i in range(1, 21, 2):
    print(i, end=' ')
print("")

print("a.",end='')
for a in range(0, 101, 10):
    print(a,end=' ')
print("")

print("b.",end='')
for b in range(20, 0, -1):
    print(b,end=' ')
print("")

star = int(input("Enter star number: "))
print("c.",end='')
print(f"Number of stars: {star}")
for c in range(0, star, 1):
    print("*",end='')
print("")

print("d.")
for d in range(0, star, 1):
    num = d+1
    for e in range(0, num, 1):
        print("*",end='')
    print("")