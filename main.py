def display_main_page(balance):
    print('Entering 1 will display the balance')
    print('Entering 2 will allow making a withdraw')
    print('Entering 3 will allow making a deposit')
    print('Entering 4 will exit the program')

    #loop:
    while True:
        choice = input('Enter the number 1 to 4: ')
        # Check for valid input before going ahead with the operation.
        if choice not in ['1', '2', '3', '4']:
            print("Invalid number. Try again\n")
            continue

        if choice == "1":
            balance = display_balance(balance)
        elif choice == "2":
            balance = make_withdraw(balance)
        elif choice == "3":
            balance = make_deposit(balance)
        elif choice == "4":
            exit_program()
            break
        else:
            print("Invalid number. Try again")

        # After each operation,
        # ask the user if user wants to perform another operation
        another_action = input("Would you like to perform another operation? (yes/no): ")
        if another_action != 'yes':
            exit_program()
            break


# Balance Display
#残高表示
def display_balance(balance):
    print(f'Your balance is ${balance:.2f}. \n')
    return balance


#Drawer Processing
#引き出しの処理
def make_withdraw(balance):
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
        return withdraw(balance, amount)
    elif choice == '6':
        try:
            amount = float(input("What is amount of money to be withdrawn: "))
            # Check for valid input before going ahead with the operation.
            if amount < 0:
                print("Invalid number. Please enter a positive number.\n")
                return balance
            return withdraw(balance, amount)

        # except number
        except ValueError:
            print("Invalid input. Please enter a numeric value\n")
            return balance
    else:
        print("Invalid choice. Please try again.\n")
        return balance


def withdraw(balance, amount):
    if amount < 0:
        print("Invalid number. Please enter a positive number\n")
    elif amount > balance:
        print("Balance is not enough\n")
    else:
        balance -= amount
        print(f'Your balance is ${balance:.2f} \n')
    return balance


#Deposit Processing
#入金処理
def make_deposit(balance):
    try:
        amount = float(input("What is amount of money to be deposit: "))
        if amount < 0:
            print("Invalid amount, please enter an amount greater than or equal to 0.\n")
            return balance

        balance += amount
        print(f'Your balance is  ${balance:.2f} \n')

    except ValueError:
        print("Invalid input. Please enter a numeric value\n")
    return balance


# Exit Program
def exit_program():
    print("Exit Program")

if __name__ == "__main__":
    display_main_page()
