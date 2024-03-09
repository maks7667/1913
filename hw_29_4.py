import psycopg2

conn = psycopg2.connect(
    dbname="your_database",
    user="your_user",
    password="your_password",
    host="your_host",
    port="your_port"
)

cur = conn.cursor()

cur.execute("INSERT INTO your_table (column1, column2) VALUES (%s, %s)", (value1, value2))

conn.commit()

cur.close()
conn.close()
