# from warnings import catch_warnings
import matplotlib.pyplot as plt
from ast import match_case


print("Welcome to the chartmaker! Please begin by choosing one of the following options: \nOption 1: Manual Data Entry \nOption 2: Enter Data From Text File \nOption 0: End the program")
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

def gettingStyles(name, opOne, one,  opTwo, two, opThree, three, opFour, four):
        userStyle = None
        while True:
                                userOption = input(f'Would you like to choose a custom {name}? Y/N  ').strip().upper()
                                if userOption == 'Y':
                                        print(f'Option 1: {opOne} \nOption 2: {opTwo} \nOption 3: {opThree} \nOption 4: {opFour}')
                                        userOption = input().strip().upper()
                                        if userOption == "1":
                                                userStyle = one
                                        elif userOption == "2":
                                                userStyle = two
                                        elif userOption == "3":
                                                userStyle = three
                                        elif userOption == "4":
                                                userStyle = four
                                        break
                                elif userOption == "N":
                                        break
                                else:
                                        print('Please Choose Y/N.')
        return userStyle        

x_axis = list()
y_axis = list()

while True:
        userOption = input("Please Enter your Option: ").strip().upper()
        match userOption.strip():
                case "1":
                        while userOption != "E":
                                userOption = input("Press 'Enter' to add value in x-axis List or 'E' to exit: ").strip().upper()
                                if userOption != "E":
                                        isFloat("Please Enter x-axis values: ", x_axis)

                        while userOption.upper() != "Q":
                                userOption = input("Press 'Enter' to add value in y-axis List or 'Q' to exit: ").strip().upper()
                                if userOption != "Q":
                                        isFloat("Please Enter y-axis values: ", y_axis)

                        print( x_axis)
                        print( y_axis)
                        plotTitle = quesAns("plot title")
                        x_axisLabel = quesAns("x-axis label")
                        y_axisLabel = quesAns("y-axis label")
                        lineStyle = gettingStyles(name = "line Style", opOne = "Solid Line", one = '-',  opTwo = "Dotted Line", two = ':', opThree = "Dashed Line", three = '--',  opFour = "Dashed/Dotted Line", four = '-.')
                        markerStyle = gettingStyles(name = "marker Style", opOne = "Circle Marker", one = 'o',  opTwo = "Star Marker", two = '*', opThree = "Diamond Marker", three = 'D',  opFour = "Hexagon Marker", four = 'H')                
                        
                        # print(plotTitle)
                        # print(x_axisLabel)
                        # print(y_axisLabel)
                        # print("Line Style: " , lineStyle)
                        # print("Marker: " , markerStyle)
                        """
                        ---- Plotting the Graph ----
                        """
                        plt.plot(x_axis, y_axis, linestyle = lineStyle, marker = markerStyle)
                        plt.title(plotTitle)
                        plt.xlabel(x_axisLabel)
                        plt.ylabel(y_axisLabel)
                        plt.show()
                        x_axis.clear()
                        y_axis.clear()

                case "2":

                        floatData= list()
                        x_axis = None
                        y_axis = None
                        try:
                                fileName = input("Please enter the file name: ")
                                fileData = open(f'{fileName}', 'r')
                                for line in fileData.readlines():
                                        lengthOfData = line.strip().split(",")
                                        floatList = [float(x) for x in lengthOfData]
                                        floatData.append(floatList)
                                        # print(floatList)
                        except Exception:
                                print("Error: File Does not exist. ", Exception)
                        if len(floatData):
                                [x_axis, y_axis] = floatData
                                # print(floatData)
                                # print(x_axis)
                                # print(y_axis)
                                plotTitle = quesAns("plot title")
                                x_axisLabel = quesAns("x-axis label")
                                y_axisLabel = quesAns("y-axis label")
                                lineStyle = gettingStyles(name = "line Style", opOne = "Solid Line", one = '-',  opTwo = "Dotted Line", two = ':', opThree = "Dashed Line", three = '--',  opFour = "Dashed/Dotted Line", four = '-.')
                                markerStyle = gettingStyles(name = "marker Style", opOne = "Circle Marker", one = 'o',  opTwo = "Star Marker", two = '*', opThree = "Diamond Marker", three = 'D',  opFour = "Hexagon Marker", four = 'H')

                                """
                                ---- Plotting the Graph ----
                                """
                                plt.plot(x_axis, y_axis, linestyle = lineStyle, marker = markerStyle)
                                plt.title(plotTitle)
                                plt.xlabel(x_axisLabel)
                                plt.ylabel(y_axisLabel)
                                plt.show()

                        
                        
                case "0":
                        # bool(int("0"))
                        print("Good Bye")
                        break
                case _:
                        print("Sorry this option is not available")




