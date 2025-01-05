def deposit():
    while True:
        amount = input("PLEASE ENTER THE AMOUNT THAT YOU GOING TO DEPOSIT :$")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be grater tha zero ")
        else:
            print("Please enter a number")
    return amount

deposit()
        
