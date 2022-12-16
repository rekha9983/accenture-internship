import mysql.connector as c
con=c.connect(host="localhost",username="root",password="Ra12ba34$$",database="my_database")
cursor=con.cursor()
Title=input("title = ")
First_name=input("Enter first name = ")
Last_name=input("enter last  name = ")
Email_id=input("enter email_id = ")
Enterprise_id=input("enter enterprise_id = ")
Project_name=input("enter project = ")
Technology=input("enter technology = ")
Manager=input("enter manager = ")
Location=input("enter location = ")


querry="INSERT INTO registeration values(Title,First_name,Last_name,Email_id,Enterprise_id,Project_name,Technology,Manager,Location)".format({},{},{},{},{},{},{},{},{})
cursor.execute(querry)
con.commit()
print("data inserted succesfully")


