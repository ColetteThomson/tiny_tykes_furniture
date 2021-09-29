import gspread
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


class hotel_manage:
    def __init__(self, rt='', s=0, p=0, r=0, t=0, a=1000, name='', address='', checkin_date='', coutdate='', rno=1):
        print("\n*****WELCOME TO THE HOTEL CALIFORNIA*****\n")
        self.rt = rt
        self.r = r
        self.t = t
        self.p = p
        self.s = s
        self.a = a
        self.name = name
        #self.address = address
        self.checkin_date = checkin_date
        #self.coutdate = coutdate
        self.rno = rno
    
    def input_name(self):
        while True:
            try:
                self.name = input('\nEnter your surname:')
                if self.name.isalpha():
                    print('Data is valid')
                    #return self.name
                    break
                else:
                    raise TypeError
            except TypeError:
                print('Please select "1" and re-enter with letters only.')
                main()
                #return False
                            
    def input_date(self):
        self.checkin_date = input("\nEnter your check in date: \n")
           #print("Your room no.:", self.rno, "\n")
    

    def room_rent(self):
        print('We have the following room types available:\n')
        print('1.  Family : £100 pn')
        print('2.  Twin Bed : £80 pps')
        print('3.  Double : £70 pps')
        print('4.  Single : £60 pp')

        x = int(input('\nPlease enter the Number of your choice (example: 1): \n'))
        n = int(input('Please enter Number of nights you would like to stay with us? (example: 2): \n'))

        if (x == 1):
            print('You have selected a Family room\n')
            self.s = 100 * n

        elif (x == 2):
            print('You have selected a Twin Bed room\n')
            self.s = 80 * n

        elif (x == 3):
            print('You have selected a Double room\n')
            self.s = 70 * n

        elif (x == 4):
            print('You have selected a Single room\n')
            self.s = 60 * n

        else:
            print('Please select a room type')
            print('Your chosen room rent is =", self.s, "\n')

    def food_purchased(self):
        print("*****RESTAURANT MENU*****")
        print('1. Dinner : £40 pp\n', '2. Breakfast : £15 pp\n', '3. Lunch : £30 pp\n', '4. Exit from Menu\n')

        while (1):
            c = int(input('Enter the Menu number of your choice.: \n'))

            if (c == 1):
                d = int(input('For how many people (example: 2): \n'))
                self.r = self.r + 40 * d

            elif (c == 2):
                d = int(input('For how many people (example: 2): \n'))
                self.r = self.r + 15 * d

            elif (c == 3):
                d = int(input('For how many people (example: 2): \n'))
                self.r = self.r + 30 * d

            elif (c == 4):
                break

            else:
                print("You've Enter an Invalid Key")
                print("Total food Cost=Rs", self.r, "\n")

    def show_final_bill(self):
        print('******HOTEL CALIFORNIA BILL******')
        print('Customer details: ')
        print('Customer name:', self.name)
        #print("Customer address:", self.address)
        print('Check in date:', self.checkin_date)
        #print("Check out date", self.coutdate)
        print('Room no.', self.rno)
        print('Your Room rent is:', self.s)
        print('Your Food bill is:', self.r)
        self.rt = self.s + self.t + self.p + self.r

        #print('Your sub total Purchased is:', self.rt)
        #print('Additional Service Charges is', self.a)
        print('Your Final Bill cost is:', self.rt + self.a, '\n')
        self.rno += 1


def main():
    a = hotel_manage()

    while (1):
        print("1.Enter Customer Data")
        print("2.Calculate Room Rent")
        print("3.Calculate Food Purchased")
        print("4.Show total cost")
        print("5.EXIT")

        b = int(input("\nEnter the number of your choice:"))

        if (b == 1):
            a.input_name()
            a.input_date()

        if (b == 2):
            a.room_rent()

        if (b == 3):
            a.food_purchased()

        if (b == 4):
            a.show_final_bill()

        if (b == 5):
            quit()


main()

"""
    def validate_string(values):
        try:
            if not isalpha():
                raise ValueError(
                    f"Please use letters of the alphabet, you entered{e}\n"
                )
        except ValueError as e:
                print(f"Invalid data: {e}, please try again.\n")
                return False
        return True """