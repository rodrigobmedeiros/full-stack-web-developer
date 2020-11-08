import psycopg2

conn = psycopg2.connect('dbname=rodrigodb user=postgres password=draGao01')
cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS todos;')

cursor.execute("""
               CREATE TABLE todos (
                   id serial PRIMARY KEY,
                   description VARCHAR NOT NULL
               );""")

cursor.execute("""
               INSERT INTO todos (description) VALUES ('rodrigo'), ('bernardo'), ('medeiros');
               """)

cursor.execute("""
               SELECT * FROM todos;
               """)

result = cursor.fetchall()
print(result)
print(len(result))

conn.commit()



cursor.close()

conn.close()