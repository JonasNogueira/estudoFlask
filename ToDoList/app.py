from flask import Flask, render_template, request

app = Flask(__name__)
list = []


@app.route("/", methods=["GET", "POST"])
def principal():
    if request.method == "POST":
        if request.form.get("item"):
            list.append(request.form.get("item"))

    return render_template("index.html", list=list)
