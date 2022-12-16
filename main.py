# That code is for insert data in table in mysql

# INSERT INTO employee(Title,first_name, last_name,email_id,Enterprise_id,Project_name,Technology,Manager,Loaction)
# VALUES
#     ('Mr','Jang','SinghUmath','Jang.SinghUmath@accenture.com','Jang.SinghUmath','AIRP','Java','Anita','Bangalore'),
#     ('Mr','Aamir','AzamAziz','Aamir.AzamAziz@accenture.com','Aamir.AzamAziz','DS','python','Padma','Chennai');
   # Mr	Ayush	Rameja	Ayush.Rameja@accenture.com	Ayush.Rameja	DE	Java	Padma	Bangalore	
#Mr	Akhil	Thella	Akhil.Thella@accenture.com	Akhil.Thella	Looker	python	Akash	Delhi	
    
   
    
# That code is for delete data from table in mysql

# DELETE FROM employee
# WHERE first_name = 'jang';



# That code is for Update 
# UPDATE employee SET Manager='Padma'
    # -> WHERE first_name='jang';



from flask import Flask ,request
from flaskext.mysql import MySQL 
mysql = MySQL() 
f=open("main.html","r")
file=f.read(encoding="utf8")
print(file)
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
       Title=request.form['Title']
       Name=request.form['name'] 
       Email=request.form['email'] 
       state=request.form['state'] 
       cursor.execute("insert into employee values (%s,%s,%s)".format(Title,Name,Email,state)) 
       con.commit() 
       return "successfully registered" 