from flask import Flask, request, render_template
import mysql.connector

app = Flask(__name)

# Replace with your database connection details
db_config = {
    'user': 'mj',
    'password': 'Passw0rd',  # Replace with your MySQL password
    'host': 'localhost',
    'database': 'mj',
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get user inputs from the form
        name = request.form['name']
        family = request.form['family']

        try:
            # Connect to the database
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()

            # Insert user input into the database
            query = "INSERT INTO user_info (name, family) VALUES (%s, %s)"
            cursor.execute(query, (name, family))
            conn.commit()

        except mysql.connector.Error as err:
            print(f"Error: {err}")

        finally:
            # Close the cursor and connection
            cursor.close()
            conn.close()

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
