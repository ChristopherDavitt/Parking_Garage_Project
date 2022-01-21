
class parking_garage:
    
    def __init__(self):
        self.ticket = {}
        self.slots = None
        self.tickets_avail = []

    def paid_ticket(self):
        ticketNumber = input("What is your ticket number? ") 
        if ticketNumber in self.ticket.keys():
            self.ticket[ticketNumber] = "paid"
        else:
            print("Ticket is not been taken. ")

    def leave(self):
        garage_leave = input("What is your ticket number? ")

        if garage_leave in self.ticket.keys() and "paid" in self.ticket[garage_leave]:
            del self.ticket[garage_leave]
            print("Thanks for parking!")
            self.tickets_avail.append(garage_leave)
    def take(self):
        enter_garage = input("You enter the garage! Press any key to take your ticket.")

        if self.tickets_avail == []:
            print("Sorry, Parking Garage is full.See you next time!")
            self.tickets_avail.append()

