# Class for Bus

class Bus:
    def __init__(self, route, seats, price):
        self.route = route
        self.seats = seats
        self.price = price
        self.booked = 0
        self.passengers = []

    # Show bus info
    def show_info(self):
        print(f"Route: {self.route} | Seats: {self.seats} | Booked: {self.booked} | Price: {self.price}")

    # Book a seat
    def book_seat(self, name):
        if self.booked < self.seats:
            self.booked += 1
            self.passengers.append(name)
            print(f"Seat booked for {name}! Ticket Price: {self.price}")
        else:
            print("No Seats are Available.")

# Class for BusSystem
class BusSystem:
    def __init__(self):
        self.buses = []

    # Add a new bus
    def add_bus(self, route, seats, price):
        self.buses.append(Bus(route, seats, price))
        print("Bus added!")

    # Show all buses
    def show_buses(self):
        for i, bus in enumerate(self.buses, 1):
            print(f"{i}.", end="")
            bus.show_info()

    # Book a seat on a bus
    def book_bus_seat(self, index, name):
        if 0 <= index < len(self.buses):
            self.buses[index].book_seat(name)
        else:
            print("Invalid bus selection.")

# Main menu loop
def main():
    system = BusSystem()
    while True:
        print("\n1. Add Bus\n2. Show Buses\n3. Book Seat\n4. Exit")
        choice = input("Choose: ")
        if choice == "1":
            system.add_bus(input("Route: "), int(input("Seats: ")), float(input("Price: ")))
        elif choice == "2":
            system.show_buses()
        elif choice == "3":
            system.show_buses()
            system.book_bus_seat(int(input("Bus number: ")) - 1, input("Passenger Name: "))
        elif choice == "4":
            break
        else:
            print("Invalid Choice.")

main()















