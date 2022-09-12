from app import app
from flask import render_template, request, redirect, flash
from app import db
from app.models import NewUser

def profile():
    user = request.args
    username = user.get("username")
    password = user.get("password")
    return render_template("profile.html", username=username, password=password)

def delete():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username == None or username == "" or password == None or password == "":
            return "Invalid parameters"

        oldUser = NewUser.query.filter(NewUser.username == username).first()

        if oldUser == None or oldUser.password != password:
            return "User does not exist or password does not match."

        try:
            db.session.delete(oldUser)
            db.session.commit()
        except Exception as err:
            print(err)
            return ("Internal server error.")
        return redirect("/index")

    return render_template("delete.html")