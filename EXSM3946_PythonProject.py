from warnings import catch_warnings


print("Welcome to the chartmaker! Please begin by choosing one of the following options: \nOption 1: Manual Data Entry \nOption 2: Enter Data From Text File")

while True:
        userOption = input("Please Enter your Option: ")
        match userOption:
                case "1":
                        print("Manual Data Entry.")
                case "2":
                        print("Entry Data from text File.")
                case "0":
                        # bool(int("0"))
                        print("Good Bye")
                        break
                case _:
                        print("Sorry this option is not available")

