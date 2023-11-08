import mysql.connector

# Replace with your database connection details
db_config = {
    'user': 'mj',
    'password': 'Passw0rd',
    'host': 'localhost',
    'database': 'mj',
}

try:
    # Connect to the database
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Execute SQL queries
    cursor.execute("SELECT * FROM mj")
    results = cursor.fetchall()

    for row in results:
        print(row)

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Close the cursor and connection
    cursor.close()
    conn.close()
