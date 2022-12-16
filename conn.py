# !C:\Users\r.a.bai\OneDrive - Accenture\python
import cgi
form=cgi.FieldStorage()
print("Content-Type:text/html")
print()
print("<h1>Welcome to python </h1>")
print("<hr/>")
print("<h1>Using input tag</h1>")
print("<body bgcolor='white'>")


Title=form.getvalue("Title")
First_name=form.getvalue("First_name")
Last_name=form.getvalue("Last_name")
Email_id=form.getvalue("Email_id")
Enterprise_id=form.getvalue("Enterprise_id")
Project_name=form.getvalue("Project_name")
Technology=form.getvalue("Technology")
Manager=form.getvalue("Manager")
Location=form.getvalue("Location")


import mysql.connector

con=mysql.connector.connect(user='root',password='Ra12ba34$$',host='localhost',database='my_database')

cur=con.cursor()

querry="INSERT INTO registeration(Title,First_name,Last_name,Email_id,Enterprise_id,Project_name,Technology,Manager,Location)".VALUES('Mr','jyoti','rani','jyoti.rani@accenture.com','jyoti.rani','myproject','python','padma','Bangalore')

# add_user = ("INSERT INTO DB.registeration(Title,First_name,Last_name,Email_id,Enterprise_id,Project_name,Technology,Manager,Location)".VALUES('Mr'','Ayush','Rameja','Ayush.Rameja@accenture.com','Ayush.Rameja','DE','Java','Padma','Bangalore'))
cur.execute(querry)

# querry=cur.execute("INSERT INTO registeration VALUES(Mr,Ayush,Rameja,Ayush.Rameja@accenture.com,Ayush.Rameja,DE,Java,Padma,Bangalore)",(Title,First_name,Last_name,Email_id,Enterprise_id,Project_name,Technology,Manager,Location))


print("<h3>record inserted successfully</h3>")
print("<a href='http:localhost/mango/index.php'>Click here to go back")