# CSC1009
def average(sum, numItems):
    return sum / numItems  # Divide the sum by the number of items


print("Average of 2 numbers")
print("Please Input 2 numbers seperated by a new line")

x = float(input())
y = float(input())
sum = x + y  # sums the 2 validated input from the user
avg = average(sum, 2)  # averages the sum by 25
print("Average is", avg)  # prints the average
