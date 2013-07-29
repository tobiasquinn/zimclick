#!/usr/bin/python

# This loads a set of test numbers into the SMS database
import sqlite3

DB = 'numbers.db'

print("Remove existing %s database" % DB)
import os
os.system("rm %s" % (DB))

print("Creating sqlite3 database %s" % DB)

conn = sqlite3.connect(DB)
# create the table
c = conn.cursor()
c.execute('''create table numbers
(number text, sent integer, delivered integer)''')
conn.commit()

testdata = [
        ('+4477xxxxxxxx', 0, 0),
        ('+4477xxxxxxxx', 0, 0),
        ('+4477xxxxxxxx', 0, 0),
        ('+4477xxxxxxxx', 0, 0),
        ('+4477xxxxxxxx', 0, 0),
        ('+4477xxxxxxxx', 0, 0),
]

for data in testdata:
    c.execute('insert into numbers values (?,?,?)', data)
conn.commit()
