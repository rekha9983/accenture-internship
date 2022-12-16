from flask import Flask , request
from flaskext.mysql import MySQL 
mysql = MySQL() 
app=Flask(__name__) 
app.config['MYSQL_DATABASE_USER'] ="root" 
app.config['MYSQL_DATABASE_PASSWORD'] = "Ra12ba34$$"
app.config['MYSQL_DATABASE_DB'] ="my_database" 
app.config['MYSQL_DATABASE_HOST'] = "localhost" 
mysql.init_app(app) 
con=mysql.connect() 
cursor=con.cursor() 
@app.route('/register',methods=['POST']) 
def register(): 
    name=request.form['name'] 
    email=request.form['email'] 
    password2=request.form['password2'] 
    birthday=request.form['birthday']
    cursor.execute("insert into table_name values (%s,%s,%s,%s)",       (name,email,password2,birthday)) 
    con.commit() 
    return "successfully registered" 