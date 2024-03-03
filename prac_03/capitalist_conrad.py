"""
CP1404/CP5632 - Practical
Capitalist Conrad wants a stock price simulator for a volatile stock.
The price starts off at $10.00, and, at the end of every day there is
a 50% chance it increases by 0 to 10%, and
a 50% chance that it decreases by 0 to 5%.
If the price rises above $1000, or falls below $0.01, the program should end.
The price should be displayed to the nearest cent (e.g. $33.59, not $33.5918232901)
"""
import random

# 设置价格变化的范围和初始价格
MIN_PRICE = 1.0  # 最低价格为 1 美元
MAX_PRICE = 100.0  # 最高价格为 100 美元
INITIAL_PRICE = 10.0  # 初始价格为 10 美元

# 设置价格变化的最大涨幅和最大跌幅
MAX_INCREASE = 0.175  # 最大涨幅为 17.5%
MAX_DECREASE = 0.05  # 最大跌幅为 5%
# 定义输出文件名
OUTPUT_FILE = "price_history.txt"

# 打开输出文件
out_file = open(OUTPUT_FILE, 'w')

price = INITIAL_PRICE
number_of_days = 0  # 初始天数为 0
print(f"Starting price: ${price:,.2f}", file=out_file)

while MIN_PRICE <= price <= MAX_PRICE:
    price_change = 0
    # generate a random integer of 1 or 2
    # if it's 1, the price increases, otherwise it decreases
    if random.randint(1, 2) == 1:
        # generate a random floating-point number
        # between 0 and MAX_INCREASE
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        # generate a random floating-point number
        # between negative MAX_DECREASE and 0
        price_change = random.uniform(-MAX_DECREASE, 0)

    price *= (1 + price_change)
    number_of_days += 1  # 每次循环迭代增加天数
    print(f"On day {number_of_days} price is: ${price:,.2f}", file=out_file)
# 关闭输出文件
out_file.close()