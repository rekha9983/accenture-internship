import mysql.connector as conn
from flask import (render_template,Flask,jsonify,request,abort as ab)

app = Flask(__name__)

def conn_db():
    return conn.connect(user='root',
                    password='Ra12ba34$$',
                    host='localhost',
                    database='my_database'
                    )


@app.route('/')
def index():
    return render_template('my.html')


@app.route('/addScore', methods=['POST'])
def add_score():
    cnx = conn_db()
    cursor = cnx.cursor()
    MatchID = request.form['matchID']
    Home_Score = request.form['homeScore']
    Away_Score = request.form['awayScore']
    print("Updating score")
    if not request.json:
        ab(400)
    cursor.execute("INSERT INTO scores (Match_ID, Home_Score, Away_Score) VALUES (%s,%s,%s,%s)",(MatchID, Home_Score, Away_Score))


    if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0')