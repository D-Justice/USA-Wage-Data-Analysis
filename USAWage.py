import sqlite3
import csv

conn = sqlite3.connect('data.sqlite')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS Data
            (ID INTEGER, position TEXT, Wage2014 INTEGER, Wage2015 INTEGER, Wage2016 INTEGER, Wage2017 INTEGER, Wage2018 INTEGER)''')

id = 0



with open('Data USA Cart.csv', newline='') as File:
    reader = csv.reader(File)
    next(reader, None)
    for column in reader:

        position = column[1]
        wage2014 = float(column[2]) if column[2] != "" else 0.0
        wage2015 = float(column[3]) if column[3] != "" else 0.0
        wage2016 = float(column[4]) if column[4] != "" else 0.0
        wage2017 = float(column[5]) if column[5] != "" else 0.0
        wage2018 = float(column[6]) if column[6] != "" else 0.0
        id = id + 1
        print(position, wage2014, wage2015, wage2016, wage2017, wage2018)
        #print(row)



        cur.execute('''INSERT OR REPLACE INTO Data(ID, position, Wage2014, Wage2015, Wage2016, Wage2017, Wage2018)
        VALUES (?, ?, ?, ?, ?, ?, ?)''', (id, position, wage2014, wage2015, wage2016, wage2017, wage2018))
conn.commit()

print('Committed: ',id, 'items!')

cur.close()
