import random
import os


class Employee:
    def employeeno(self):
        self.not_used()
        return random.randrange(100, 500)

    def not_used(self):
        pass


obj2 = Employee()


class TicketBooking:
    def serialno(self):
        self.not_used()
        return random.randrange(1000, 5000)

    def not_used(self):
        # this function is made just to avoid 'static warning'.
        pass


obj1 = TicketBooking()
while True:
    choice = input('\n1>New Ticket\n2>Search\n3>Modify\n4>cancel ticket\n5>exit')

    if choice == '1':      # NEW TICKET
        serialnum = obj1.serialno()
        BookingName = input('enter name ')
        departure = input('enter place of departure')
        NumOfTickets = input('enter number of tickets')
        with open('flight_book.txt', 'a') as file:
            file.write('\nserial no. = ' + str(serialnum) +
                       '\nname = ' + str(BookingName) + '\n' 
                       'departing from '+'\''+str(departure)+'\'' + '\n'
                       'you have booked ' + str(NumOfTickets)+'ticket(s)')
        print('data entered successfully!\n')
        print('\nserial no. of your ticket = ' + str(serialnum) +
              '\nname = ' + str(BookingName) + '\n' 
              'departing from '+'\''+str(departure)+'\'' + '\n'
              'you have booked ' + str(NumOfTickets) + 'ticket(s).' + '\n\n')

    if choice == '2':      # SEARCH
        TicketNum = input('enter the serial num of ticket ')
        if TicketNum.isalpha():
            print('please enter only numbers.')
            continue
        p = 2
        with open('flight_book.txt', 'r') as file1:
            search_lines = file1.readlines()
        for i, line in enumerate(search_lines):
            if TicketNum in line.split():
                p = 1
                for l in search_lines[i:i + 4]:
                    print(l, end='')
        if p == 2:
            print('Record not found !')

    if choice == '3':    # MODIFY
        pass

    if choice == '4':    # CANCEL TICKET
        j = -100
        TicketNum = input('enter the serial num of ticket ')
        if TicketNum.isalpha():
            print('please enter only numbers.')
            continue
        z = 2
        with open('flight_book.txt', 'r') as file1:
            search_lines = file1.readlines()
            with open('flight_temp.txt', 'w') as tempFile:
                for i, line in enumerate(search_lines):
                    if TicketNum in line.split():
                        for l in search_lines[i:i + 4]:
                            j = i
                            z = 1

                    elif TicketNum not in line.split():
                        if i == j+1 or i == j+2 or i == j+3:
                            continue
                        else:
                            tempFile.write(line)
                if z == 2:
                    print('Record not found !')
                elif z == 1:
                    print('Records successfully updated.')
        os.remove('flight_book.txt')
        os.rename('flight_temp.txt', 'flight_book.txt')
    if choice == '5':      # EXIT
        exit()
