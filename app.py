from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/save', methods=['POST','GET'])
def store():

    mydb = mysql.connector.connect(
        user = "root",
        password = "",
        database="practice"
    )

    mycursor = mydb.cursor()
    if request.method=='POST':
        register = request.form
        Name = register['Name']
        Fathername = register['fathername']
        Mothername = register['mothername']
        email = register['email']
        mobile = register['mob']
        nprvsch = register['prvSchool']

        mycursor.execute("insert into register (Name,fathername,mothername,email,mob,nameprvsch)values(%s,%s,%s,%s,%s,%s)",(Name, Fathername, Mothername, email, mobile, nprvsch))
        mydb.commit()
        mycursor.close()

        message = "You are registered Soon the dates for entrance test will be announced and you will recieve the same on your registered email"
        return render_template("index.html", message=message)
if __name__=='__main__':
    app.run(port='0.0.0.0')
