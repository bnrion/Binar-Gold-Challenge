import sqlite3
import csv

conn = sqlite3.connect('preprocess.db')

cursor = conn.cursor()

cursor.execute("""
            CREATE TABLE IF NOT EXISTS mytable (
            Tweet text, 
            HS text, 
            Abusive text,
            HS_Individual text,
            HS_Group text,
            HS_Religion text,
            HS_Race text,
            HS_Physical text,
            HS_Gender text,
            HS_Other text
            )
""")

with open('preprocessed_indonesian_toxic_tweet.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader)
    for row in reader:
        cursor.execute("""
            INSERT INTO mytable (Tweet, HS, Abusive)
            VALUES(?, ?, ?)
        """, row[:3])

conn.commit()
conn.close()
