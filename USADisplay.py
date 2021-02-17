import sqlite3



conn = sqlite3.connect('data.sqlite')
cur = conn.cursor()


count = 0
nullcount = 0
ASCDSC = input("Would you like to see the Highest or Lowest wages? ")
howmany = input("How many itterations would you like?")
howmany = int(howmany)
#Organises SQL data in ascending order and prints x number of iterations
if ASCDSC == "Highest" or ASCDSC == "highest":

    if howmany == str(howmany) or howmany >= 531:
        print("ERROR: Please Enter a number between 1-530!")
        quit()

    cur.execute('SELECT * FROM Data ORDER BY Wage2018 DESC')

    print("Top", howmany, "wages in the US (As of 2018): \n")
#Pulls all the data for the wage2018 column(skipping NULL cells), converts to floating point
#and prints job and latest wage data
    for row in cur:
        if row[6] == "" or row[6] == "Average Wage (2018)":
            nullcount += 1
            continue
        count = count + 1
        wage = float(row[6])
        wage = round(wage, 2)
        if count > howmany:
            break
        else:
            print("\n",row[1],"-------------", "$", wage)
    print("\n===Skipped", nullcount,"entries due to insufficient data===")
#Organises SQL data in descending order and prints x number of iterations
elif ASCDSC == "Lowest" or ASCDSC == "lowest":

    if howmany == str(howmany) or howmany >= 531:
        print("ERROR: Please Enter a number between 1-530!")
        quit()
    cur.execute('SELECT * FROM Data ORDER BY Wage2018 ASC')
    print("Bottom", howmany, "wages in the US (As of 2018): \n")
#Pulls all the data for the wage2018 column(skipping NULL cells), converts to floating point
#and prints job and latest wage data
    for row in cur:
        if row[6] == "" or row[6] == "Average Wage (2018)":
            nullcount += 1
            continue
        count = count + 1
        wage = float(row[6])
        wage = round(wage, 2)
        if count > howmany:
            break
        else:
            print("\n", row[1],"-------------", "$", wage)
    print("\n===Skipped", nullcount,"entries due to insufficient data===")

else:
    print("ERROR: Please enter either 'Highest' or 'Lowest'")

#Ask if user would like to see additional data such as: Growth rate over 4 years, median pay,highest growth rate etc
highGrowRate = 0.0
highGrowJob = None
count = 0
YN = input('\n\nWould you like to see additional data? Y/N ')
if YN == "Y" or YN == "y":
    print("\nGrowth Rate of these positions: ")
    for row in cur:
        count = count + 1
        if count >= howmany:
            break
        else:
            try:
                median = (((row[3] - row[2]) / row[3]) * 100) + (((row[4] - row[3]) / row[4]) * 100) + (((row[5] - row[4]) / row[5]) * 100) + (((row[6] - row[5]) / row[6]) * 100)

                #=====BUG====== - getting traceback saying row[x] is str but is actually float as show by type(row[x])

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
