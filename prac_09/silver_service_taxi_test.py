from silver_service_taxi import SilverServiceTaxi

def main():
    people = 2
    my_taxi = SilverServiceTaxi("Hummer", 200, 4)
    my_taxi.start_fare()
    my_taxi.drive(18)
    total_fare = my_taxi.calculate_fare()  # Calculate total fare
    print(my_taxi)
    print(f"Fare: ${total_fare:.2f}")
    print(f"For each one people Fare: ${(total_fare-4.5)/people + 4.5:.2f}")
if __name__ == "__main__":
    main()