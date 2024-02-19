number = int(input("Number of items:"))
total = 0
for item in range(0, number, 1):
    Price = float(input("Price of item: "))
    total = total + Price
if total > 100:
    total = total * 90 /100
else:
    pass
print(f"Total price for 3 items is ${total}")