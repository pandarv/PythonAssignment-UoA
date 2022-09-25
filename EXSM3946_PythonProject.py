# from warnings import catch_warnings


print("Welcome to the chartmaker! Please begin by choosing one of the following options: \nOption 1: Manual Data Entry \nOption 2: Enter Data From Text File")
def isFloat(prompt, vari):
        isTrue = False
        while isTrue != True:
                try:
                        inputVal = float(input(prompt))
                        vari.append(inputVal)
                        isTrue = True
                        print(inputVal)
                except:
                        print("Please Enter correct Number format ")
                        isTrue = True
                        isFloat(prompt, vari)

x_axis = list()
y_axis = list()

while True:
        userOption = input("Please Enter your Option: ")
        match userOption.strip():
                case "1":
                        print("Manual Data Entry.")
                        # xAxisList = input("Please Enter x-axis values: ")
                        # x_AxisEntry = ""
                        while userOption != "E":
                                userOption = input("Please choose options: ")
                                if userOption is not "E":
                                        isFloat("Please Enter x-axis values: ", x_axis)
                                        print(userOption)
                        # x_axis.append(xAxisList)
                        print( x_axis)
                        yAxisList = input("Please Enter y-axis values: ")
                case "2":
                        print("Entry Data from text File.")
                case "0":
                        # bool(int("0"))
                        print("Good Bye")
                        break
                case _:
                        print("Sorry this option is not available")






# print(isFloat(("Please Enter Number: ")))
# print(inputVal)