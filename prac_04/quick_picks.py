import random

# Constants
MIN_NUMBER = 1
MAX_NUMBER = 99
NUMBERS_PER_LINE = 6

def main():
    num_quick_picks = int(input("How many quick picks? "))
    for i in range(num_quick_picks):
        quick_pick = generate_quick_pick()
        print(" ".join(f"{number:2}" for number in quick_pick))

def generate_quick_pick():
    quick_pick = []
    while len(quick_pick) < NUMBERS_PER_LINE:
        random_number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if random_number not in quick_pick:
            quick_pick.append(random_number)
    return sorted(quick_pick)

main()