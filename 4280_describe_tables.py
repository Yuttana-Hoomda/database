from getpass import getpass
from mysql.connector import connect, Error
from connect_via_env import get_connect

def describeTable(table):
    cursor.execute(table)
    print(f"{table}' table structure")
    description = cursor.fetchall()
    for row in description:
        print(row)
    print("-"* 50)

try:
    with get_connect() as connection:
        create_db_query = "CREATE DATABASE IF NOT EXISTS movies_db"
        create_movies_table_query = """
            CREATE TABLE IF NOT EXISTS movies(
                id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(100),
                release_year YEAR(4),
                genre VARCHAR(100),
                collection_in_mil INT
            )
        """
        show_movies_table_query = "DESCRIBE movies"
        
        create_reviewers_table_query = """
            CREATE TABLE IF NOT EXISTS reviewers(
                id INT AUTO_INCREMENT PRIMARY KEY,
                first_name VARCHAR(100),
                last_name VARCHAR(100)
            )
        """
        show_reviewers_table_query = "DESCRIBE reviewers"
       
        create_ratings_table_query = """
            CREATE TABLE IF NOT EXISTS ratings(
                movie_id INT,
                reviewer_id INT,
                rating DECIMAL(2,1),
                FOREIGN KEY(movie_id) REFERENCES movies(id),
                FOREIGN KEY(reviewer_id) REFERENCES reviewers(id),
                PRIMARY KEY(movie_id, reviewer_id)
            )
        """
        show_ratings_table_query = "DESCRIBE ratings"
        with connection.cursor() as cursor:
            cursor.execute(create_db_query)
            print("Database created successfully")

            cursor.execute(create_movies_table_query)
            cursor.execute(create_reviewers_table_query)
            cursor.execute(create_ratings_table_query)
            connection.commit()
            print("Table 'movies' created successfully")
            print("Table 'reviewers' created successfully")
            print("Table 'ratings' created successfully")

            describeTable(show_movies_table_query)
            describeTable(show_reviewers_table_query)
            describeTable(show_ratings_table_query)

except Error as e:
    print(f"Error at {e}")

finally:
    if connection and connection.is_connected():
        connection.close()
        print("Database connection closed.")
