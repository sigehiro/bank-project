

# balance
balance = 1000

def display_main_page():
    print('Entering 1 will display the balance')
    print('Entering 2 will allow making a withdraw')
    print('Entering 3 will allow making a deposit')
    print('Entering 4 will exit the program')

    #loop:
    while True:
        choice = input('Enter the number 1 to 4: ')

        if choice == "1":
            display_balance(balance)
        elif choice == "2":
            make_withdraw(balance)
        elif choice =="3":
            make_deposit(balance)
        elif choice =="4":
            exit_program()
            break
        else:
            print("Invalid number. Try again")



#残高表示
def display_balance(balance):
    print(f'Your balance is ${balance:.2f}. \n')


#引き出しの処理
def make_withdraw(balance):

    while True:
        try:
        #TODO ここでの入力で「０９」とか入れると＄991と読み込まれてしまう。
            amount = float(input("What is amount of money to be withdrawn: "))
            if amount > balance:
                print("Balance is not enough\n")
            else:
                balance -= amount
                print(f'Your balance is ${balance:.2f} \n')
            
                return balance
        # except number
        except ValueError:
            print("Invalid input. Please enter a numeric value\n")


#入金処理
def make_deposit(balance):
    print("入金を行います")

# プログラム終了
def exit_program():
    print("プログラムを終了します。")


if __name__ == "__main__":
    display_main_page()