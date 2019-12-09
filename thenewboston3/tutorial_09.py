# Exception

while True:
    try:
        number = int(input("Whats your fav number? \n"))
        print(18/number)
        break
    except ValueError:
        print("Make sure and enter a number")
    except ZeroDivisionError:
        print("Don't pick zero")
    finally:
        print("No matter of the code worked,this has been run at once")