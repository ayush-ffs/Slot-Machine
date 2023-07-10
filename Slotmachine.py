import random
# global constant for constant we use capital letter s in python
MAX_BET_LINES = 3
MAX_BETS = 100
MIN_BETS = 1
# collecting money from player
ROWS = 3
COLS = 3
all_symbols = {
    "A":2,
    "B":3,
    "C":4,
    "D":5
}
symbol_values = {
    "A":5,
    "B":4,
    "C":3,
    "D":2
}
def get_slot_machine_spin(rows, cols, symbols):
    symbols = []
    for symbol ,symbol_count in all_symbols.items():
        symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        currentsym = symbols[:]
        for _ in range(rows):
            value = random.choice(currentsym)
            column.append(value)
            currentsym.remove(value)
        columns.append(column)
    return columns
def print_slot_machine(columns):
    # here columns ka actually not the roes of the slots it's actual vertical lines in our
    # matrix, so we have to print by the transposing of matrix
    for rows in range(len(columns[0])):
        for i , colum in enumerate(columns):
            if i != len(colum)-1:
                # by default in python if we don't use end or give conditions what we want it will take new line \n .
                print(colum[rows], end="|")
            else:
                print(colum[rows] , end="")

        print()

def check_wining(columns , lines , values , bet):
    wining_of_every_line = 0
    wining_lines = []
    for line in range(lines):
        # Here we are checking in row col no. in vertical because it's actually in horizontal
        sym = columns[0][line]
        for col in columns:
            symbol_to_check = col[line]
            if sym != symbol_to_check:
                break
        else:
            wining_of_every_line += values[sym]*bet
            wining_lines.append(line)

    return wining_of_every_line, wining_lines


def deposit():
    while True:
        amount = input("Enter the amount to be deposited? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Enter the amount greater than 0.")
        else:
            print("Enter the valid amount.")

    return amount
def get_num_of_lines():
    while True:
        lines = input("Enter the number of line of bet 1-"+str(MAX_BET_LINES)+":")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_BET_LINES:
                break
            else:
                print("Enter the amount greater than 0.")
        else:
            print("Enter the valid amount.")
    return lines

def get_bet():
    while True:
        amount = input("Enter the amount to be bet one each line?: $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BETS <= amount <= MAX_BETS:
                break
            else:
                print("Enter the amount between"+str(MIN_BETS)+"-"+str(MAX_BETS)+".")
        else:
            print("Enter the valid amount.")

    return amount
def  spin(balance):
    lines = get_num_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print("You doesn't have enough balance.your current balance is :&" + str(balance))
        else:
            break

    print("you are betting $" + str(bet) + " one each line.your total bet is :$" + str(total_bet))
    slots = get_slot_machine_spin(ROWS, COLS, all_symbols)
    print_slot_machine(slots)
    winings, wining_lines = check_wining(slots, lines, symbol_values, bet)
    print("Your winings is:&" + str(winings) + ".")
    if winings > 0:
        print("your wining lines are:", *wining_lines)


    return winings - total_bet

def main():
    balance = deposit()

    while True:
        print("your current balance is : $" + str(balance))
        spin_to_start = input("Enter if you want to play or for quit press q: ")
        if spin_to_start == "q":
            break

        balance += spin(balance)

    print("You left with balance: $" + str(balance))


main()
