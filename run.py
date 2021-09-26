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

inventory = SHEET.worksheet('inventory')

#data = inventory.get_all_values()
#print(data)

def menu_display():
    print('Welcome to Tiny Tykes Furniture Inventory')
    print('(1) Update Inventory Item')
    print('(2) Search Inventory')
    print('(3) Add New Inventory Item')
    print('(4) Delete Inventory Item')
    print('(5) Print Inventory Report')
    print('(6) Quit')

    OPTION = int(input('Enter number choice: '))
    menu_option(OPTION)

def menu_option(OPTION):
    if OPTION == 1:
        update_inventory()
    elif OPTION == 2:
        search_inventory()
    elif OPTION == 3:
        add_inventory()
    elif OPTION == 4:
        delete_inventory()
    elif OPTION == 5:
        print_inventory()
    elif OPTION == 6:
        exit()

menu_display()
