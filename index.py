import main



print("\n<<<< Here is Humber Bank >>>>\nHello\n")


# (Tentative) Correct PIN code :（仮）正しいPINコード
correct_pin = '1234'

# Accepts only 4-digit character entries (up to 3 entries)
#4桁の文字の入力のみを受け付ける(3回まで入力可能)
for attempt in range(3):
    input_pin_num = input('Enter the PIN number: ')
    if input_pin_num.isdigit() and input_pin_num == correct_pin:
        print("Success\n")
        # Default account value
        initial_balance = 1000
        main.display_main_page(initial_balance)
        break
    else:
        print('Invalid entry.')
else:
    print('You have made three mistakes and are finished.')

