This sends a message to a set of nunbers held in an SQLITE3 database.

It consists of two parts - a server script and a sending script

The database schema is as follow:

type      field
================
TEXT    - number
INTEGER - sent (number of send tries - 0 for not sent)
INTEGER - delivered (has it been delivered - 0 for unknown, 1 for delivered)

The script takes the file message.txt as the message to send

It takes blocks of 45 messages and sends them in a burst. The server receives
delivery reports and updates the database.

