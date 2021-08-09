from flask import *
import sqlite3
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html");

@app.route("/add_record")
def add_record():
    return render_template("add_record.html")

@app.route("/saverecord",methods = ["POST","GET"])
def saveRecord():
    msg = "msg"
    if request.method == "POST":
        try:
            name = request.form["name"]
            ph = request.form["ph"]
            email = request.form["email"]
            address = request.form["add"]
            print(name)
            print(ph)
            print(address)
            print(email)
            with sqlite3.connect("yellow_pages.db") as connection:
                print("test")
                cursor = connection.cursor()
                print("test1")
                cursor.execute("INSERT into Company_Info (Company_Name, Phone, Email, Address) values (?,?,?,?)",(name, ph, email, address))
                
                connection.commit()
                msg = "Company Info successfully Added"
        except:
            connection.rollback()
            msg = "We can not add Company details to the database"
        finally:
            return render_template("success_record.html",msg = msg)
            connection.close()


@app.route("/display")
def display():
    connection = sqlite3.connect("yellow_pages.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Company_Info")
    print("test")
    rows = cursor.fetchall()
    return render_template("display.html",rows = rows)

@app.route("/delete_company")
def delete_company():
    return render_template("delete_company.html")

@app.route("/deleterecord",methods = ["POST"])
def deleterecord():
    ph = request.form["ph"]
    with sqlite3.connect("yellow_pages.db") as connection:

        cursor = connection.cursor()
        cursor.execute("select * from Company_Info where Phone=?", (ph,))
        rows = cursor.fetchall()
        if not rows == []:

            cursor.execute("delete from Company_Info where Phone = ?",(ph,))
            msg = "Student record successfully deleted"
            return render_template("delete_response.html", msg=msg)

        else:
            msg = "Enetered phone number doesn't exist!"
            return render_template("delete_response.html", msg=msg)

@app.route("/update_record")
def update_record():
    return render_template("update_record.html")


@app.route("/updaterecord",methods = ["POST"])
def updaterecord():
    ph = request.form["ph"]
    name=request.form["name"]
    email = request.form["email"]
    address =request.form["add"]
    with sqlite3.connect("yellow_pages.db") as connection:

        cursor = connection.cursor()
        cursor.execute("select * from Company_Info where Phone=?", (ph,))
        rows = cursor.fetchall()
        if not rows == []:

            cursor.execute("update Company_Info set Company_Name= ?, Email = ?, Address = ? where Phone = ?",(name,email, address, ph ,))
            msg = "Record updated successfully "
            return render_template("delete_response.html", msg=msg)

        else:
            msg = "Phone doesn't exist!"
            return render_template("delete_response.html", msg=msg)
        



if __name__ == "__main__":
    app.run(debug = True)  