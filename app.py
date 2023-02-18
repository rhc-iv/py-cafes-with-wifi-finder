from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    conn = sqlite3.connect('cafes.db')
    c = conn.cursor()
    c.execute("SELECT DISTINCT city FROM cafes")
    cities = c.fetchall()
    conn.close()
    return render_template('index.html', cities=cities)


@app.route('/cafes', methods=['POST'])
def cafes():
    city = request.form['city']
    conn = sqlite3.connect('cafes.db')
    c = conn.cursor()
    c.execute("SELECT * FROM cafes WHERE city LIKE ?", ('%' + city + '%',))
    cafes = c.fetchall()
    conn.close()
    return render_template('cafes.html', cafes=cafes)


if __name__ == '__main__':
    app.run(debug=True)
