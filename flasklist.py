import os
from flask import Flask, redirect, render_template, request
from random import choice
import json

app=Flask(__name__)

welcome_message = ["Hi", "Hello", "Bonjour", "Ciao", "Hola"]

items = [
    "Buy computer",
    "Learn Python"
    ]

@app.route("/")
def get_index():
    welcome = choice(welcome_message)
    return render_template("index.html", items=items, welcome=welcome)
    
@app.route("/new_task", methods=["POST"])
def create_task():
    task = request.form['task_to_do']
    items.append(task)
    
    with open("data/list.json","w") as f:
        data = json.dumps(items)
        f.write(data)
    
    return redirect("/")



if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)), debug=True)