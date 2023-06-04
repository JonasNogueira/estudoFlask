from flask import Flask, render_template, request

app = Flask(__name__)
list = []
diario = []


@app.route("/toDoList", methods=["GET", "POST"])
def principal():
    if request.method == "POST":
        if request.form.get("item"):
            list.append(request.form.get("item"))

    return render_template("index.html", list=list)


@app.route("/notasAlunos", methods=["GET", "POST"])
def notas():
    if request.method == "POST":
        if request.form.get("aluno") and request.form.get("nota"):
            diario.append(
                {"aluno": request.form.get("aluno"), "nota": request.form.get("nota")}
            )
    return render_template("professor.html", diario=diario)
