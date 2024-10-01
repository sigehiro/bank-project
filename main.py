def display_main_page():
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
        elif choice =="3":
            make_deposit()
        elif choice =="4":
            exit_program()
            break
        else:
            print("Invalid number. Try again")



#残高表示
def display_balance():
    print('残高を表示')

#引き出しの処理
def make_withdraw():
    print("引き出す金額は？")

#入金処理
def make_deposit():
    print("入金を行います")

# プログラム終了
def exit_program():
    print("プログラムを終了します。")


if __name__ == "__main__":
    display_main_page()