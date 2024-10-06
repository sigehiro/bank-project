

# balance
balance = 1000

def display_main_page():
    global balance
    print('Entering 1 will display the balance')
    print('Entering 2 will allow making a withdraw')
    print('Entering 3 will allow making a deposit')
    print('Entering 4 will exit the program')

    #loop:
    while True:
        choice = input('Enter the number 1 to 4: ')

        if choice == "1":
            display_balance()
        elif choice == "2":
            make_withdraw()
        elif choice == "3":
            make_deposit()
        elif choice == "4":
            exit_program()
            break
        else:
            print("Invalid number. Try again")



#残高表示
def display_balance():
    global balance
    print(f'Your balance is ${balance:.2f}. \n')


#引き出しの処理
def make_withdraw():
    global balance
    print("Choose an amount to withdraw:")
    print("1. $20")
    print("2. $40")
    print("3. $60")
    print("4. $80")
    print("5. $100")
    print("6. Option")

    choice = input("Enter the number of the choice: ")
    if choice in ['1', '2', '3', '4', '5']:
        options_withdraw = [20, 40, 60, 80, 100]
        amount = options_withdraw[int(choice) - 1]
        withdraw(amount)
        

    elif choice == '6':
        try:
            amount = float(input("What is amount of money to be withdrawn: "))
            withdraw(amount)

        # except number
        except ValueError:
            print("Invalid input. Please enter a numeric value\n")

    else:
        print("Invalid choice. Please try again.\n")

def withdraw(amount):
    global balance
    if amount < 0:
        print("Invalid number. Please enter a positive number\n")
    elif amount > balance:
        print("Balance is not enough\n")
    else:
        balance -= amount
        print(f'Your balance is ${balance:.2f} \n')


#入金処理
def make_deposit():
    print("入金を行います")

# プログラム終了
def exit_program():
    print("プログラムを終了します。")


if __name__ == "__main__":
    display_main_page()