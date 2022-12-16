
from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('registraion.html')
@app.route('/create',methods=["POST"])
def getvalue():
    Title=request.form['Title']
    First_name=request.form['First_name']
    Last_name=request.form['Last_name']
    Email_id=request.form['Email_id']
    Enterprise_id=request.form['Enterprise_id']
    Project_name=request.form['Project_name']
    Technology=request.form['Technology']
    Manager=request.form['Manager']
    Location=request.form['Location']
    
    return render_template('pass.html',Title=Title,First_name=First_name,Last_name=Last_name,Email_id=Email_id,Enterprise_id=Enterprise_id,Project_name=Project_name,Technology=Technology,Manager=Manager,Location=Location)
    
if __name__  == '__main__':
    app.run(debug=True)
# getvalue()

# index()



# file = open("registration.html", "r")
# print (file.read())

