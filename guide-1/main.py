import csv
from datetime import datetime
import os



xlist = []
ylist = []

while True:
    try:
        xlist.append(int(input("X: ")))
        ylist.append(int(input("Y: ")))
        
    except ValueError:
        continue
    except EOFError: 
        if len(xlist) > len(ylist):

            while True:
                try:
                    ylist.append(int(input("\nPlease input 1 more Y: ")))   
                    break
                except:
                    continue
        else:
             break


op = input("\nOperator (Valid: *, /, +, - ): ").strip()


def write(x, y, operator):
    file_exists = os.path.isfile('log.txt')
    with open('log.txt', "a", newline="") as csvfile:
            fieldnames = ["x", " y", " operator", " time"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if not file_exists:
                writer.writeheader()

            time = datetime.now()
            detailed_format = time.strftime("%A, %B %d, %Y at %I:%M %p")
            writer.writerow({"x": x, " y": y, " operator": operator, " time": detailed_format})

#4 functions have been used. Only counting functions that have parentheses.
zipped = list(zip(xlist, ylist))
for x, y in zipped:
    if op == "*":
        print(x * y)
        write(x, y, op)
    elif op == "/":
        print(x / y)
        write(x, y, op)
    elif op == "+":
        print(x + y)
        write(x, y, op)
    elif op == "-":
        print(x - y)
        write(x, y, op)
    else:
        while True:
            op = input("\nOperator (Valid: *, /, +, - ): ").strip()
            if op == "*":
                print(x * y)
                write(x, y, op)
                break
            elif op == "/":
                print(x / y)
                write(x, y, op)
                break
            elif op == "+":
                print(x + y)
                write(x, y, op)
                break
            elif op == "-":
                print(x - y)
                write(x, y, op)
                break
