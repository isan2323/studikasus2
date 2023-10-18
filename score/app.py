# import SQL untuk menggunakan bahasa SQL dalam python
from cs50 import SQL
# import tools utk website
from flask import Flask, flash, jsonify, redirect, render_template, request, session

app = Flask(__name__)

db = SQL("sqlite:///score.db")

@app.route('/', methods=["GET", "POST"]) #root route
def index(): #function index
    if request.method == "POST":
        name = request.form.get("name")
        score = request.form.get("score")
        db.execute("INSERT INTO score (name, score) values(?,?)", name, score)
        return redirect("/")
    else:
        students = db.execute("select * from score")
        return render_template("index.html", students=students)
    
# @app.route("/edit/<id>", methods=["GET", "POST"])
# def edit():
#     if request.method == 

@app.route("/edit/<id>", methods=["GET", "POST"])
def edit_data(id):
    if request.method == "GET":
        score = db.execute("SELECT * FROM score WHERE id = ?", id)[0]
        print(score)
        return render_template("edit.html", score=score)
    elif request.method == "POST":
        score_name = request.form.get("name")
        score_score = request.form.get("score")
        db.execute('UPDATE score set name = ?, score = ? where id = ?', score_name, score_score, id)
        return redirect("/") 
    
@app.route("/Delete/<id>", methods=["GET"])
def Delete_data(id):
    db.execute("Delete from score where id = ?", id)
    return redirect("/")