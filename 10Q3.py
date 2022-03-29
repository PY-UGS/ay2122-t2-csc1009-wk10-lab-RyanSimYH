def getModuleCode(moduleCode):
    modules = {
        "CSC1009": "Object Oriented Programming",
        "CSC1007": "Operating Systems",
        "CSC1008": "Data Structures & Algorithms",
        "CSC1006": "Mathematics 2"
    }
    return modules.get(moduleCode)  # obtain the value from the Dictionary and return it for printing


def PrintAllOdd(start, end):
    print("The odd numbers between", start, " to ", end, "are:")
    for i in range(start, end,-1):  # iterate through all the numbers between the start and the end
        if i % 2 == 1:  # if there is a remainder when a number is divided by 2, it is an odd number
            print(i)  # print out the odd number


print("Obtain Module Name")
while (True):  # code will only exit when a valid input is provided
    userInput = input().upper()  # obtain input from user
    if userInput.__contains__("CSC100"):  # check if user input matches the module code
        break
    else:
        print("Invalid Module Code! Please Try Again!")  # prompt user for valid input
print(getModuleCode(userInput))
PrintAllOdd(102, 66)
