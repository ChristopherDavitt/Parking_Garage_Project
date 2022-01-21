
class Parking_Garage:
    
    def __init__(self):
        self.ticket = {}
        self.tickets_avail = []

    def paid_ticket(self):
        ticketNumber = int(input("What is your ticket number? "))
        
        if ticketNumber in self.ticket.keys():
            self.ticket[ticketNumber] = "paid"
            print(f"Ticket number {ticketNumber} has been paid") 
        else:
            print("Ticket is not been taken... Please Try Again ")

    def leave(self):
        garage_leave = int(input("What is your ticket number? "))

        if garage_leave in self.ticket.keys() and "paid" in self.ticket[garage_leave]:
            del self.ticket[garage_leave]
            print("Thanks for parking!")
            self.tickets_avail.append(garage_leave)
        else:
            print("Your ticket has either not been taken, or not been paid yet... Please Try Again")

    def take(self):
        enter_garage = input("You enter the garage! Press any key to take your ticket. ")
        if self.tickets_avail == []:
            print("Sorry, Parking Garage is full. See you next time!")
        else:
            your_ticket = self.tickets_avail.pop()
            self.ticket[your_ticket] = ''
            print(f"Your ticket is number {your_ticket}")

def run(spots_in_garage):
    your_garage = Parking_Garage()
    for i in range(1, spots_in_garage + 1):
        your_garage.tickets_avail.append(i)
    while True:
        print(f"Tickets In Parking Garage {your_garage.ticket}")
        print(f"Tickets Available: {your_garage.tickets_avail}")
        print("""
        Choose an option:
        [1] Enter Garage
        [2] Pay your ticket
        [3] Leave Garage""")
        option = int(input(": "))

        if option == 1:
            your_garage.take()
        if option == 2:
            your_garage.paid_ticket()
        if option == 3:
            your_garage.leave()
run(10)