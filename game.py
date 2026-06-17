number = 7
while True:
    try:
        userinput=int(input("ENTER YOUR NUMBER "))
        if userinput>number:
            print("Too High ")
        elif userinput<number:
            print("Too Low")
        else:
            print("Your Guess is correct")
            break

    except ValueError:
        print("INVALID INPUT ")