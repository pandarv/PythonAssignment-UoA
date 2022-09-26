# from warnings import catch_warnings
import matplotlib.pyplot as plt

from ast import match_case


print("Welcome to the chartmaker! Please begin by choosing one of the following options: \nOption 1: Manual Data Entry \nOption 2: Enter Data From Text File")
def isFloat(prompt, vari):
        isTrue = False
        while isTrue != True:
                try:
                        inputVal = float(input(prompt))
                        vari.append(inputVal)
                        isTrue = True
                except:
                        print("Please Enter correct Number format ")
                        isTrue = True
                        isFloat(prompt, vari)

def quesAns(title):
        while True:
                userSelection = input(f'Would you like a {title}? ').strip().upper()
                if userSelection == "Y":
                        variableName = input(f'Please enter {title} ').strip().capitalize()
                        return variableName
                elif userSelection == "N":
                        break 
                else:
                        print("Please Enter 'Y' or 'N'.")

x_axis = list()
y_axis = list()

while True:
        userOption = input("Please Enter your Option: ")
        match userOption.strip():
                case "1":
                        print("Manual Data Entry.")
                        # xAxisList = input("Please Enter x-axis values: ")
                        # x_AxisEntry = ""
                        while userOption.upper() != "E":
                                userOption = input("Press 'Enter' to add value in x-axis List or 'E' to exit: ")
                                if userOption != "E":
                                        isFloat("Please Enter x-axis values: ", x_axis)

                        while userOption.upper() != "Q":
                                userOption = input("Press 'Enter' to add value in y-axis List or 'Q' to exit: ")
                                if userOption is not "Q":
                                        isFloat("Please Enter y-axis values: ", y_axis)

                        print( x_axis)
                        print( y_axis)
                        plotTitle = quesAns("plot title")
                        x_axisLabel = quesAns("x-axis label")
                        y_axisLabel = quesAns("y-axis label")                
                        
                        print(plotTitle)
                        print(x_axisLabel)
                        print(y_axisLabel)
                        plt.plot(x_axis, y_axis)
                        plt.show()
                        # while True:
                        #         userOption = input("Would you like to choose a custom line style? Y/N  ").strip().upper()
                        #         match userOption:
                        #                 case 'Y':
                        #                         print("Choose from the options")
                        #                 case 'N':
                        #                         break
                        #                 case _:
                        #                         print('Please Choose Y/N.')
                        x_axis.clear()
                        y_axis.clear()

                case "2":
                        print("Entry Data from text File.")
                case "0":
                        # bool(int("0"))
                        print("Good Bye")
                        break
                case _:
                        print("Sorry this option is not available")




