# myguitars.py

import csv
from guitar import Guitar, read_guitars_from_csv

def display_guitars(guitars):
    for guitar in guitars:
        print(f"{guitar.name} - Year: {guitar.year}, Cost: ${guitar.cost}")

def add_new_guitars(guitars):
    while True:
        name = input("Enter the name of the guitar (or 'quit' to stop adding): ")
        if name.lower() == 'quit':
            break
        year = input("Enter the year of the guitar: ")
        cost = input("Enter the cost of the guitar: ")
        if year.lower() == 'quit' or cost.lower() == 'quit':
            break
        guitars.append(Guitar(name, year, cost))

def write_guitars_to_csv(guitars, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Year', 'Cost'])  # Write header row
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])

def main():
    guitars = read_guitars_from_csv('guitars.csv')
    print("Guitars from CSV:")
    display_guitars(guitars)
    
    print("\nSorting guitars by year (oldest to newest):")
    guitars.sort()
    display_guitars(guitars)
    
    add_new_guitars(guitars)
    
    write_guitars_to_csv(guitars, 'guitars.csv')
    print("New guitars have been added and written to guitars.csv")


main()
