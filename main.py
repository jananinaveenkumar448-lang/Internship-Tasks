import utils
def converter():
    while True:
        print("---TEMPERATURE CONVERTER---")
        print("1.Celsius to Fahrenheit")
        print("2.Fahrenheit to Celsius")
        print("3.Exit")
        choice=input("Enter Choice: ")
        if choice=="1":
            c=float(input("Enter Celsius: "))
            f=(c*9/5)+32
            print(f"{c}C={f:.2f}F")
        elif choice == "2":
            f = float(input("Enter Fahrenheit: "))
            c = (f - 32) * 5/9
            print(f"{f}F = {c:.2f}C")
        elif choice == "3":
            break
        else:
            print("Invalid choice")
def guessing_game():
    number = 7
    while True:
        userinput = input("ENTER YOUR NUMBER: ")
        if not utils.is_valid_number(userinput):
            print("INVALID INPUT")
            continue
        userinput = int(userinput)
        if userinput > number:
            print("Too High")
        elif userinput < number:
            print("Too Low")
        else:
            print("Correct!")
            break
while True:
    print("\n====== MAIN MENU ======")
    print("1. Temperature Converter")
    print("2. Guessing Game")
    print("3. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        converter()
    elif choice == "2":
        guessing_game()
    elif choice == "3":
        break
    else:
        print("Invalid choice")
            