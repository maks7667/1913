import psycopg2

conn = psycopg2.connect(
    dbname="your_database",
    user="your_user",
    password="your_password",
    host="your_host",
    port="your_port"
)

cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS your_table (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255),
        age INTEGER
    )
""")

cur.execute("INSERT INTO your_table (name, age) VALUES (%s, %s)", ("John", 30))

cur.execute("SELECT * FROM your_table")
rows = cur.fetchall()
for row in rows:
    print(row)

cur.execute("UPDATE your_table SET age = %s WHERE name = %s", (35, "John"))

cur.execute("DELETE FROM your_table WHERE name = %s", ("John",))

conn.commit()

cur.close()
conn.close()
