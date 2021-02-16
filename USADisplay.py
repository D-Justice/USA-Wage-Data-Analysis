import sqlite3
import ssl
import re


conn = sqlite3.connect('data.sqlite')
cur = conn.cursor()


count = 0
ASCDSC = input("Would you like to see the Highest or Lowest wages? ")

if ASCDSC == "Highest" or ASCDSC == "highest":
    howmany = input("How many itterations would you like?")
    howmany = int(howmany)
    if howmany == str(howmany) or howmany >= 531:
        print("ERROR: Please Enter a number between 1-530!")
        quit()

    cur.execute('SELECT * FROM Data ORDER BY Wage2018 DESC')

    print("Top", howmany, "wages in the US (As of 2018): \n")

    for row in cur:
        if row[6] == "" or row[6] == "Average Wage (2018)":
            continue
        count = count + 1
        wage = float(row[6])
        wage = round(wage, 2)
        if count > howmany:
            break
        else:
            print(row[1],"-------------", "$", wage)

elif ASCDSC == "Lowest" or ASCDSC == "lowest":

    howmany = input("How many itterations would you like?")
    howmany = int(howmany)

    if howmany == str(howmany) or howmany >= 531:
        print("ERROR: Please Enter a number between 1-530!")
        quit()
    cur.execute('SELECT * FROM Data ORDER BY Wage2018 ASC')
    print("Bottom", howmany, "wages in the US (As of 2018): \n")

    for row in cur:
        if row[6] == "" or row[6] == "Average Wage (2018)":
            continue
        count = count + 1
        wage = float(row[6])
        wage = round(wage, 2)
        if count > howmany:
            break
        else:
            print(row[1],"-------------", "$", wage)

else:
    print("ERROR: Please enter either 'Highest' or 'Lowest'")
