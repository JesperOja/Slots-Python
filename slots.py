import random

MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100

ROWS = 3
COLS = 3

symbol_count = {
    "X": 2,
    "Y": 3,
    "Z": 4,
    "R": 6,
    "F": 6
}

values = {
    "X": 6,
    "Y": 5,
    "Z": 4,
    "R": 2,
    "F": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for col in columns:
            symbol_to_check = col[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line +1)
    
    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        
        columns.append(column)

    return columns

def print_slots(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) -1:
                print(column[row], end=" | ")
            else:
                print(column[row])

def deposit():
    while True:
        amount = input("What would you like to deposit? €")
        
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than zero")
        
        else:
            print("Please enter a number!")
    
    return amount

def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES})? ")
        
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Lines must be greater than zero")
        
        else:
            print("Please enter a number!")
    
    return lines

def get_bet(balance, lines):
    while True:
        amount = input("What would you like to bet on each line? €")
        total_bet = int(amount) * lines
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                if total_bet <= balance:
                    break
                else:
                    print(f"You cannot bet that much, your balance is {balance}")
            else:
                print(f"Bet must be equal or greater than {MIN_BET}")
        
        else:
            print("Please enter a number!")
    
    return amount, total_bet


def slots(balance):
    lines = get_number_of_lines()
    bet, total_bet = get_bet(balance, lines)
    
    print(f"You are betting €{bet} on {lines} lines. Total bet: €{total_bet}")
    
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slots(slots)
    
    winnings, winning_lines = check_winnings(slots, lines, bet, values)
    print(f"You won {winnings}.")
    print("Winning lines: ", *winning_lines)
    return winnings - total_bet


def main():
    answer = input("Welcome to virtual text slots! Would you like to play with shitty odds and without fear of actually loosing money? (y/n) ")
    if answer == "y": 
        
        balance = deposit()
        total_deposit = balance
        while True:
            print(f"Current balance is €{balance}")
            spin = input("Press enter to play, d to deposit more, q to quit: ")
            if spin == "q":
                break
            
            if spin == "b":
                new_deposit = deposit()
                balance += new_deposit
                total_deposit += new_deposit
            else:
                if balance == 0:
                    print(f"You cannot play more with balance of €{balance}, deposit more or quit")
                else:
                    balance += slots(balance)
            
        print(f"You left with total deposit: €{total_deposit} | Balance: €{balance}")
        print(f"Total networth: €{balance-total_deposit}")
    else:
        print("Have a nice day!")

main()