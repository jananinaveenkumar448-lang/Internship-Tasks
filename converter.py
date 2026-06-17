while True:
    print("----TEMPERATURE CONVERTER----")
    print("1.CELSIUS TO FAHRENHEIT ")
    print("2.FAHRENHEIT TO CELSIUS ")
    print("3.EXIT")
    choice=input("ENTER CHOICE(1,2,3) ")
    if choice=="1":
        c=float(input("ENTER CELSIUS "))
        f=(c*9/5)+32
        print(f"{c}C: {f:.2f}F")
    elif choice=="2" :
      f = float(input("Enter Fahrenheit: "))
      c = (f-32)*5/9
      print(f"{f}F: {c:.2f}C")
    elif choice=="3":
       print("EXITING ")
       break
    else:
       print("YOH INVALID CHOICE")