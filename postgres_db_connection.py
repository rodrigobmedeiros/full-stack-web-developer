import psycopg2

conn = psycopg2.connect('dbname=rodrigodb user=postgres password=draGao01')
cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS todos;')

cursor.execute("""
CREATE TABLE todos (
    id serial PRIMARY KEY,
    description VARCHAR NOT NULL
);""")

conn.commit()

cursor.close()

conn.close()