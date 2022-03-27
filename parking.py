available_spaces = { 
        1:"unpaid",
        2:"unpaid",
        3:"unpaid",
        4:"unpaid",
        5:"unpaid",
        6:"unpaid",
        7:"unpaid",
        8:"unpaid",
        9:"unpaid",
        10:"unpaid"
}
parking_garage = {}

class Parking():

    def empty_spaces(self):
        if available_spaces:
            print(f'Available Spaces: {len(available_spaces)}')
        else:
            print("There aren't any available spaces.")

    def parking_tickets(self):
        ticket = list(available_spaces)[0]
        parking_garage.update({ticket:available_spaces[ticket]})        
        del available_spaces[ticket]
        print(f'Your ticket is {ticket}')
        
    def pay_ticket(self):
        while True:
            ticket_number_response = int(input("What is your ticket #?\n '0' to quit\n "))
            if ticket_number_response == 0:
                break
            elif ticket_number_response in parking_garage.keys():
                confirm = input(f'Your ticket is {ticket_number_response}, is that correct? Y/N ')
                while True:
                    if confirm.lower() == 'y':
                        payment = input('Please pay ticket.')
                        if payment.lower() == 'card' or payment.lower() == 'cash':
                            parking_garage[ticket_number_response] = 'paid'
                            print("Thank you for your payment.")
                            break
                    elif confirm.lower() == 'n':
                        break
                    else:
                        print("Invalid")
            else:
                print("Invalid")


    def leave_garage(self):
        while True:
            show_ticket = int(input("Type '0' to quit\nShow your ticket number: "))
            if show_ticket == 0: 
                break
            elif parking_garage.get(show_ticket) == 'paid':
                print("Please exit.")
                parking_garage[show_ticket] = "unpaid"
                available_spaces.update({int(show_ticket):parking_garage[show_ticket]})
                del parking_garage[show_ticket]
                break
            elif parking_garage.get(show_ticket) == 'unpaid':
                print("Please pay your ticket.")    
            else:
                print("Invalid")
                
    def ui(self):
        while True:
            response = input("Which would you like to do:\n 'Show Spaces'/'Take Ticket'/'Pay Ticket'/'Leave'/'Quit'\n")
            if response.lower() == 'quit':
                print("Please visit Sinners Garage again!")
                break
            elif response.lower() == 'show spaces':
                self.show_spaces()
            elif response.lower() == 'take ticket':
                self.take_ticket()
            elif response.lower() == 'pay ticket':
                self.pay_ticket()
            elif response.lower() == 'leave':
                self.leave_garage()
            else:
                print("Invalid Response, Try Again")

run = Parking()
run.ui()