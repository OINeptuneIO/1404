# guitar.py

import csv

class Guitar:
    def __init__(self, name, year, cost):
        self.name = name
        self.year = int(year)
        self.cost = float(cost)
        
    def __lt__(self, other):
        return self.year < other.year

def read_guitars_from_csv(filename):
    guitars = []
    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            name, year, cost = row
            if name == 'Name':  # Skip header row
                continue
            guitars.append(Guitar(name, year, cost))
    return guitars
