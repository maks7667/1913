import psycopg2

conn = psycopg2.connect(
    dbname="your_database",
    user="your_user",
    password="your_password",
    host="your_host",
    port="your_port"
)

cur = conn.cursor()

cur.execute("DELETE FROM your_table WHERE condition")

conn.commit()

cur.close()
conn.close()
