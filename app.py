from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('netflixweb.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def open():
    return render_template('open.html')

# @app.route('/dashboard')
# def dashboard():
#     return render_template('dashboard.html')

# @app.route('/open')
# def dashboard():
#     return render_template('open.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        gmail = request.form['gmail']
        password = request.form['password']
        connection = get_db_connection()
        user = connection.execute('SELECT * FROM users WHERE gmail = ? AND password = ?',
                                  (gmail, password)).fetchone()
        connection.close()

        if user:
            return redirect(url_for('watching'))
        else:
            return "Incorrect gmail or password."

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        full_name = request.form['full_name']
        gmail = request.form['gmail']
        password = request.form['password']
        # confirm_password = request.form['confirm_password']
        phone_number = request.form['phone_number']
        country = request.form['country']

        # if password != confirm_password:
        #     return "Passwords do not match."

        connection = get_db_connection()
        connection.execute('''INSERT INTO users (full_name, gmail, password, phone_number, country)
                              VALUES (?, ?, ?, ?, ?)''',
                           (full_name, gmail, password, phone_number, country))
        connection.commit()
        connection.close()
        return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/dash')
def dash():
    return render_template('dash.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/watching')
def watching():
    return render_template('watching.html')

if __name__ == '__main__':
    app.run(debug=True)
