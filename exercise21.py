import os
import mysql.connector

username = os.environ.get("DB_USERNAME")
password = os.environ.get("DB_PASSWORD")
# Establish a connection to MySQL
mydb = mysql.connector.connect(host="localhost", user=username, password=password)

# Create a cursor object
mycursor = mydb.cursor()


# create a database named "<your_name>_<your_id>_db", # such as “manee_5829_db”
def create_database():
    mycursor.execute("CREATE DATABASE IF NOT EXISTS yuttana_4280_db")
    print("Database created successfully")


# Create table
def create_table():
    mycursor.execute("USE yuttana_4280_db")
    mycursor.execute(
        """
    CREATE TABLE IF NOT EXISTS students(
        student_id INT PRIMARY KEY,
        first_name VARCHAR(50),
        last_name VARCHAR(50),
        age INT,
        major VARCHAR(50),
        gpa FLOAT
    )
    """
    )
    print("Table 'students' created successfully")


# Problem 1: Insert data
# (5829, "Manee", "Jaidee", 20, "Computer Science", 3.8)
# (1002, "Jane", "Smith", 22, "Engineering", 3.9)
# (1003, "Mike", "Johnson", 21, "Biology", 3.5)
def insert_data():
    insert_students_query = """
            INSERT INTO movies
            VALUES
            (5829, "Manee", "Jaidee", 20, "Computer Science", 3.8),
            (1002, "Jane", "Smith", 22, "Engineering", 3.9),
            (1003, "Mike", "Johnson", 21, "Biology", 3.5)
    """
    mycursor.execute(insert_students_query)
    print("insert 'students' successfully")

# Problem 2: Select data with conditions
def select_data():
    mycursor.execute("""
        select student_id, first_name, last_name, age, major, gpa
        from students
        where age = 20             
    """)
    print("select 'students who have age is 20' successfully")

# Problem 3: Update data
def update_data():
    mycursor.execute("""
        update students
        set first_name = yuttana, last_name = hoomda             
        where age = 20             
    """)
    print("update 'students first namd and last name who have age = 20' successfully")

# Problem 4: Delete data
def delete_data():
    mycursor.execute("""
        delete
        from students
        where age = 20             
    """)
    print("delete 'students who have age = 20' successfully")

# Execute all functions
create_database()
create_table()
insert_data()
select_data()
update_data()
delete_data()

# Close the cursor and connection
mycursor.close()
mydb.close()
