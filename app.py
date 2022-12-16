from flask import Flask,request,render_template
app=Flask(__name__)

@app.route("/insert")
def index():
    return render_template('registration.html')

if __name__  == '__main__':
    app.run(debug=True)