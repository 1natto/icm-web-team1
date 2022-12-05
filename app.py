from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("index.html")

@app.route("/submit", methods=['GET'])
def submit():
    name = request.args.get("name")
    code = request.args.get("code")
    folderpath = "./code"
    prewritten_tag  = ".cpp"
    user_filename = "chonphong"
    filename = user_filename + prewritten_tag
    fullpath = os.path.join(folderpath,filename)
    filepath = os.path.join(folderpath,name)
    if not os.path.exists(filepath):
        os.makedirs(filepath)

    with open(os.path.join(filepath, filename), "w") as f:
        full_txt = code
        f.write(full_txt)
    return render_template("submit.html")
