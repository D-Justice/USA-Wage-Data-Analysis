import sqlite3
import csv

conn = sqlite3.connect('data.sqlite')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS Data
            (ID INTEGER, position TEXT, Wage2014 INTEGER, Wage2015 INTEGER, Wage2016 INTEGER, Wage2017 INTEGER, Wage2018 INTEGER)''')

id = 0



with open('Data USA Cart.csv', newline='') as File:
    reader = csv.reader(File)
    for column in reader:
        position = column[1]
        wage2014 = column[2]
        wage2015 = column[3]
        wage2016 = column[4]
        wage2017 = column[5]
        wage2018 = column[6]
        id = id + 1
        print(position, wage2014, wage2015, wage2016, wage2017, wage2018)
        #print(row)

        cur.execute('''INSERT OR REPLACE INTO Data(ID, position, Wage2014, Wage2015, Wage2016, Wage2017, Wage2018)
        VALUES (?, ?, ?, ?, ?, ?, ?)''', (id, position, wage2014, wage2015, wage2016, wage2017, wage2018))
conn.commit()

print('Committed: ',id, 'items!')

cur.close()
