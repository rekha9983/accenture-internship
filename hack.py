from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('registration.html')
@app.route('/create',methods=["POST"])
def getvalue():
    if request.method=="POST":
        Title=request.form.get['Title']
        First_name=request.form.get['First_name']
        Last_name=request.form.get['Last_name']
        Email_id=request.form.get['Email_id']
        Enterprise_id=request.form.get['Enterprise_id']
        Project_name=request.form.get['Project_name']
        Technology=request.form.get['Technology']
        Manager=request.form.get['Manager']
        Location=request.form.get['Location']
    
        return render_template('pass.html',Title=Title,First_name=First_name,Last_name=Last_name,Email_id=Email_id,Enterprise_id=Enterprise_id,Project_name=Project_name,Technology=Technology,Manager=Manager,Location=Location)
    
if __name__  == '__main__':
    app.run(debug=True)
