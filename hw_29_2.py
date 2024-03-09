import psycopg2

conn = psycopg2.connect(
    dbname="your_database",
    user="your_user",
    password="your_password",
    host="your_host",
    port="your_port"
)

cur = conn.cursor()

cur.execute("SELECT * FROM your_table WHERE your_condition LIMIT 1")

row = cur.fetchone()

print(row)

cur.close()
conn.close()
