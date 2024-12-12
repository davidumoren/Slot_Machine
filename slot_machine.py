import random

MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 10
ROWS = 3
COLS = 3

symbol_count = {

    "A":2,
    "B":4,
    "C":6,
    "D":8
}

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
   
    columns = [ ]
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
           value  = random.choice(current_symbols)
           current_symbols.remove(value)
           column.append(value)
        columns.append(column) 


    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row],  end="|")
            else:
               print(column[row], end="") 
        print()

def deposit():
    while True:
        amount = input("What amount would you want to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("AMOUNT MUST BE GREATER THAN 0.00")

        else:
            print("Please Enter a number!")
    return amount



def bet():
    while True:
        amount = input("What amount would you want to bet? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET :
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}")

        else:
            print("Please Enter a number!")
    return amount



def get_number_of_lines():

    while True:
        lines = input(f"Enter the number of lines between 1 - {str(MAX_LINES)}: ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number ")

        else:
            print("Please Enter a number!")
    return lines


def main():
    balance = deposit()
    lines =  get_number_of_lines()
    while True:
        bet_amount = bet()
        total_bet = bet_amount * lines
        if total_bet > balance:
            print(f"you do not have enough amount to place a bet. Your current balance is ${balance}")
        else:
            break
        
    print(f"you are betting ${bet_amount} on {lines} lines. TOTAL bet equals {total_bet}")
    
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
main()