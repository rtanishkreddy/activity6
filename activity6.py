# display a title
import csv

# a file in the current directory
FILENAME = "test7.csv"


def write_trips(entries):
    with open(FILENAME, 'w') as file:
        writer = csv.writer(file)
        writer.writerows(entries)


print("Writing complete")
print("The Miles Per Gallon program")
print()

entries = []
entries.append("Distance, Gallons, MPG")
while True:
    # get input from the user
    miles_driven = float(input("Enter miles driven:\t\t"))
    gallons_used = float(input("Enter gallons of gas used:\t"))

    # calculate and round miles per gallon
    mpg = miles_driven / gallons_used
    mpg = round(mpg, 2)
    entries.append(str(miles_driven) + "      \t\t" + str(gallons_used) + "   \t" + str(mpg))

    # display the result
    for row in entries:
        print(row)
    print("More entries(y or n)?: ")
    choice = (input())
    if choice != 'y':
        write_trips(entries)
        break
print("Bye")
