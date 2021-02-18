import sqlite3



conn = sqlite3.connect('data.sqlite')
cur = conn.cursor()


count = 0

nullcount = 0
ASCDSC = input("Would you like to see the Highest or Lowest wages? ").lower()
howmany = input("How many itterations would you like?")
howmany = int(howmany)
def highest():
    global count
    global nullcount
    if howmany == str(howmany):
        print("ERROR: Please Enter a number between 1-530!")
        quit()

    cur.execute('SELECT * FROM Data WHERE Wage2018 > 0 ORDER BY Wage2018 DESC')

    print("Top", howmany, "wages in the US (As of 2018): \n")
#Pulls all the data for the wage2018 column(skipping NULL cells), converts to floating point
#and prints job and latest wage data
    for row in cur:
        if row[6] == 0:
            nullcount += 1
            continue
        count = count + 1
        wage = round(row[6], 2)
        if count > howmany:
            break
        else:
            print("\n",row[1],"-------------", "$", wage)
            print("\n===Skipped", nullcount,"entries due to insufficient data===")
def lowest():
    global count
    global nullcount
    if howmany == str(howmany):
        print("ERROR: Please Enter a number between 1-530!")
        quit()
    cur.execute('SELECT * FROM Data WHERE Wage2018 > 0 ORDER BY Wage2018 ASC')
    print("Bottom", howmany, "wages in the US (As of 2018): \n")
#Pulls all the data for the wage2018 column(skipping NULL cells), converts to floating point
#and prints job and latest wage data

    for row in cur:
        if row[6] == 0:
            nullcount += 1
            continue
        count = count + 1
        wage = round(row[6], 2)
        if count > howmany:
            break
        else:
            print("\n",row[1],"-------------", "$", wage)
    print("\n===Skipped", nullcount,"entries due to insufficient data===")
#Organises SQL data in ascending order and prints x number of iterations

if ASCDSC == "highest":
    highest()

#Organises SQL data in descending order and prints x number of iterations
elif ASCDSC == "lowest":
    lowest()

else:
    print("ERROR: Please enter either 'Highest' or 'Lowest'")

#Ask if user would like to see additional data such as: Growth rate over 4 years, median pay,highest growth rate etc
highGrowRate = 0.0
highGrowJob = None
count = 0

YN = input('\n\nWould you like to see additional data? Y/N ').lower()
if YN == "y":
    print("\nGrowth Rate of these positions: ")
    if ASCDSC == "highest":
        try:
            cur.execute('SELECT * FROM Data WHERE Wage2018 > 0 ORDER BY Wage2018 DESC')
        except:
            pass
    elif ASCDSC == "lowest":
        cur.execute('SELECT * FROM Data WHERE Wage2018 > 0 ORDER BY Wage2018 ASC')

    else:
        print("ERROR: Please type either Y or N to continue")

    for row in cur:
        count = count + 1
        if count >= howmany + 1:
            break
        else:
            try:
                median = (((row[3] - row[2]) / row[3]) * 100) + (((row[4] - row[3]) / row[4]) * 100) + (((row[5] - row[4]) / row[5]) * 100) + (((row[6] - row[5]) / row[6]) * 100)

                median = round(median, 2)
                print("\nGrowth of",row[1],"= %",median, "average per year")
            except Exception as i:
                print("\nError finding historical data for:",row[0], row[1])
                continue

            if median > highGrowRate:
                highGrowJob = row[1]
                highGrowRate = median
    print("\n\n\nHighest growth rate from 2016 to 2018 in the US was: ",
    highGrowJob,"with %", highGrowRate, "average growth rate")

else:
    quit()
