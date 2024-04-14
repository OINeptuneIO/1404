from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

def display_taxis(taxis):
    """Display the available taxis."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

def main():
    print("Let's drive!")
    current_taxi = None
    bill_to_date = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    
    while True:
        print("q)uit, c)hoose taxi, d)rive")
        choice = input(">>> ").lower()

        if choice == 'q':
            print(f"Total trip cost: ${bill_to_date:.2f}")
            print("Taxis are now:")
            display_taxis(taxis)
            break
        elif choice == 'c':
            print("Taxis available: ")
            display_taxis(taxis)
            try:
                taxi_choice = int(input("Choose taxi: "))
                current_taxi = taxis[taxi_choice]
                print(f"Bill to date: ${bill_to_date:.2f}")
            except (ValueError, IndexError):
                print("Invalid taxi choice")
        elif choice == 'd':
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
                print(f"Bill to date: ${bill_to_date:.2f}")
            else:
                try:
                    distance = float(input("Drive how far? "))
                    flagfall = 0
                    fare1 = current_taxi.drive(distance)
                    fare = 0
                    if current_taxi.name == 'Limo' or current_taxi.name == 'Hummer':
                        flagfall=4.5
                        fare = (fare1*(1.23*current_taxi.fanciness))+flagfall
                    else:
                        flagfall=0
                        fare = fare1*1.23
                    bill_to_date += fare
                    print(f"Your {current_taxi.name} trip cost you ${fare}")
                    print(f"Bill to date: ${bill_to_date:.2f}")
                except ValueError:
                    print("Invalid distance")
        else:
            print("Invalid option")
            print(f"Bill to date: ${bill_to_date:.2f}")

if __name__ == "__main__":
    main()
