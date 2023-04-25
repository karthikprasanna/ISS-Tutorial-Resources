import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table = "creaTE TABLE animals (id int, name text, age int, color text)"
# cursor.execute(create_table)

query = "INSERT INTO animals VALUES (1, 'cat', 2, 'black')"
cursor.execute(query)

animals = [
    (2, 'dog', 3, 'brown'),
    (3, 'rabbit', 1, 'white'),
    (4, 'bird', 2, 'green'),
    (5, 'snake', 4, 'brown'),
]
cursor.executemany("INSERT INTO animals VALUES (?, ?, ?, ?)", animals)

# connection.commit()

# select_query = "SELECT * FROM animals"
# value_returned = cursor.execute(select_query)
# for row in value_returned:
#     print(row)

# select_query = "SELECT id, name FROM animals"
# for row in cursor.execute(select_query):
#     print(row)

# create table with primary key, unique and not null
# create_table = "CREATE TABLE users1 (id int PRIMARY KEY, username text UNIQUE, password text NOT NULL)"
# cursor.execute(create_table)

# users = [
#     (1, 'jose', 'asdf'),
#     (2, 'rolf', 'None'),
# ]

# cursor.executemany("INSERT INTO users1 VALUES (?, ?, ?)", users)

# select_query = "SELECT * FROM users"
# for row in cursor.execute(select_query):
#     print(row)

select_query = "SELECT * FROM animals"
cursor.execute(select_query)
print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone())

print(cursor.fetchmany(2))


# select_query = "SELECT * FROM animals"
# cursor.execute(select_query)
# print(cursor.fetchmany(2))

# select_query = "SELECT * FROM animals"
# cursor.execute(select_query)
# print(cursor.fetchall())

# select_query = "SELECT * FROM animals WHERE age > 1"
# for row in cursor.execute(select_query):
#     print(row)

# select_query = "SELECT * FROM animals WHERE age > 1 AND color = 'black'"
# for row in cursor.execute(select_query):
#     print(row)

# query = "UPDATE animals SET age = 4 WHERE name = 'cat'"
# cursor.execute(query)

# select_query = "select * from animals"
# for row in cursor.execute(select_query):
#     print(row)

# query = "DELETE FROM animals WHERE name = 'cat'"
# cursor.execute(query)

# select_query = "SELECT * FROM animals"
# for row in cursor.execute(select_query):
#     print(row)

# select_query = "SELECT DISTINCT color FROM animals" 
# for row in cursor.execute(select_query):
#     print(row)

# select_query = "SELECT COUNT(DISTINCT color) FROM animals"
# for row in cursor.execute(select_query):
#     print(row)

# select_query = "SELECT * FROM animals ORDER BY age ASC"
# for row in cursor.execute(select_query):
#     print(row)

# select_query = "SELECT * FROM animals ORDER BY age DESC LIMIT 2"
# for row in cursor.execute(select_query):
#     print(row)

# avg, count, max, min, sum
# select_query = "SELECT AVG(age) FROM animals"
# for row in cursor.execute(select_query):
#     print(row)

# select_query = "SELECT COUNT(*) FROM animals"
# for row in cursor.execute(select_query):
#     print(row)

# select_query = "SELECT MAX(age) FROM animals"
# for row in cursor.execute(select_query):
#     print(row)

# select_query = "SELECT MIN(age) FROM animals"
# for row in cursor.execute(select_query):
#     print(row)

# select_query = "SELECT SUM(age) FROM animals"
# for row in cursor.execute(select_query):
#     print(row)

# select_query = "SELECT * FROM animals WHERE name LIKE '%n%'"
# for row in cursor.execute(select_query):
#     print(row)

# select_query = "SELECT color, COUNT(*) FROM animals GROUP BY color"
# for row in cursor.execute(select_query):
#     print(row)

# select_query = "SELECT id, name, age + 1 FROM animals"
# for row in cursor.execute(select_query):
#     print(row)

drop_table = "DROP TABLE animals"
cursor.execute(drop_table)

connection.close()

