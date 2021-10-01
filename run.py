import gspread
from datetime import datetime
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('tiny_tykes_furniture')


#self.res_no += 1
print("***WELCOME TO THE HOTEL CALIFORNIA***")
print('*...welcome message...*')


class Hotel_booking:
    def __init__(self, rt='', s=0, r=0, a=1000, name='', address='', check_in='', res_no=1):
        #print("\n*****WELCOME TO THE HOTEL CALIFORNIA*****")
        self.rt = rt
        self.r = r
        self.s = s
        self.a = a
        self.name = name
        self.check_in = check_in
        self.res_no = res_no

    def input_name(self):
        while True:
            try:
                self.name = input('\nEnter your surname: \n')
                if self.name.isalpha():
                    print('Data is valid')
                    break
                else:
                    raise TypeError
            except TypeError:
                print('Invalid data. Please re-enter using letters only.\n')

    def check_in_date(self):
        while True:
            try:
                self.check_in = input('\nEnter your check in date (dd/mm/yyyy): \n')
                if self.check_in != datetime.strptime(self.check_in, '%d/%m/%Y').strftime('%d/%m/%Y'):
                    raise ValueError
                return True
            except ValueError:
                print('Invalid date. Please try again (dd/mm/yyyy):\n')

        return

    def room_rent(self):
        print('\nHotel Room Types Available')
        print('--------------------------')
        print('1.  Family : £100 pn')
        print('2.  Twin Bed : £80 pps')
        print('3.  Double : £70 pps')
        print('4.  Single : £60 pp')

        while True:
            try:
                x = int(input('\nEnter the Number of your required Room Type (example: 1): \n'))
                n = int(input('\nEnter Number of nights you wish to stay with us (example: 2): \n'))
                
                if (x == 1):
                    print('Your choice: FAMILY room for ' + str(n) + ' night/s.\n')
                    self.s = 100 * n
                    return True

                elif (x == 2):
                    print('Your choice: TWIN BED room for ' + str(n) + ' night/s.\n')
                    self.s = 80 * n
                    return True

                elif (x == 3):
                    print('Your choice: DOUBLE room for ' + str(n) + ' night/s.\n')
                    self.s = 70 * n
                    return True

                elif (x == 4):
                    print('Your choice: SINGLE room for ' + str(n) + ' night/s.\n')
                    self.s = 60 * n
                    return True

                else:
                    raise ValueError
                
            except ValueError:
                print('Invalid data. Please try again\n')
        
        return

    def food_purchased(self):
        print('\nMeal/s Options')
        print('--------------')
        print(' 1. Dinner : £40 pp\n', '2. Breakfast : £15 pp\n',
              '3. Lunch : £30 pp\n', '4. EXIT from Restaurant Menu\n')

        while (1):
            c = int(input('Enter a number.\nMultiple items may be selected individually: \n'))
            
            if (c == 1):
                d = int(input('For how many people (example: 2): \n'))
                print('You have chosen: DINNER for ' + str(d) + '\n')
                self.r = self.r + 40 * d

            elif (c == 2):
                d = int(input('For how many people (example: 2): \n'))
                print('You have chosen: BREAKFAST for ' + str(d) + '\n')
                self.r = self.r + 15 * d

            elif (c == 3):
                d = int(input('For how many people (example: 2): \n'))
                print('You have chosen: LUNCH for ' + str(d) + '\n')
                self.r = self.r + 30 * d

            elif (c == 4):
                print('Exiting the restaurant menu...')
                return

            else:
                print("Invalid entry. Please try again.\n")

        return

    def show_final_bill(self):
        print('\n******HOTEL CALIFORNIA BILL******')
        print('Customer Details: ')
        print('Your Name:', self.name)
        print('Your Check-in Date:', self.check_in)
        print('Your Reservation Number: ', self.res_no)
        print('Your Room Cost: £', self.s)
        print('Your Meal/s Cost: £', self.r)
        self.rt = self.s + self.r
        print('Your Total Final Bill (inc VAT): £', self.rt, '\n')
        #self.res_no += 1
        print('NB: Should you wish to make any changes to')
        print('your booking - please call us on 0090-1234567')
        print('**** We hope you enjoy your stay! ****')


def main():
    a = Hotel_booking()

    while True:
        user1 = int(input('\nPress "1" to complete Guest Details (example: 1): \n'))
        if (user1 == 1):
            a.input_name()
        else:
            print('You must press "1" to continue.')
    
        user2 = int(input('\nPress "2" to complete Check-in Date (example: 2): \n'))
        if (user2 == 2):
            a.check_in_date()
        else:
            print('You must press "2" to continue.')
    
        user3 = int(input('\nPress "3" to calculate Room Cost (example: 3): \n'))
        if (user3 == 3):
            a.room_rent()
        else:
            print('You must press "3" to continue.')
    
        user4 = int(input('\nPress "4" to calculate Meal/s Cost (example: 4): \n'))
        if (user4 == 4):
            a.food_purchased()
        else:
            print('You must press "4" to continue.')
    
        user5 = int(input('\nPress "5" to show your Final Bill (example: 5): \n'))
        if (user5 == 5):
            a.show_final_bill()
        else:
            print('You must press "5" to continue.')
    
        user6 = int(input('\nPress "6" to EXIT (example: 6): \n'))
        if (user6 == 6):
            quit()
        else:
            quit()


main()


"""
def input_message():
    while True:
        user = input('\nPress enter to continue: \n')
        if user == "":
            print('yes!!')
            main()
            break
        else:
            print('You must press enter to continue.')
"""




"""
    def validate_string(values):
        try:
            if not isalpha():
                raise ValueError(
                    f"Please use numbers, you entered{e}\n"
                )
        except ValueError as e:
                print(f"Invalid data: {e}, please try again.\n")
                return False
        return True 
        """

"""
    print('\nMAIN MENU')
    print('---------')
    print('1. Enter Customer Data')
    print('2. Calculate Room Cost')
    print('3. Calculate Meal/s Cost')
    print('4. Show Final Bill')
    print('5. EXIT')
    """

