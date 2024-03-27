from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("portfolio.html")

@app.route("/project1")
def project1():
    return render_template("projects.html", 
    project_num="Проект №1", 
    project_name='City Builder "URBAN UTOPIA"', 
    project_info="Мобільна гра в жанрі City Builder", 
    link="https://github.com/Prostokishyn/DEEP-lom-DARK-FANTASY", 
    image="/static/project1.jpg", 
    project_tech="Unity, C#")

@app.route("/project2")
def project2():
    return render_template("projects.html", 
    project_num="Проект №2", 
    project_name="Практична робота №6", 
    project_info="Розробка додатків із реалізацією ієрархії класів.", 
    link="https://github.com/Prostokishyn/Practical6", 
    image="/static/project2.jpg", 
    project_tech="Python")

@app.route("/project3")
def project3():
    return render_template("projects.html", 
    project_num="Проект №3",
    project_name="Практична робота №2", 
    project_info="Робота із масивами, словниками та стрічками.", 
    link="https://github.com/Prostokishyn/practical2", 
    image="/static/project3.jpg", 
    project_tech="Python")

@app.route("/project4")
def project4():
    return render_template("projects.html", 
    project_num="Проект №4", 
    project_name="Практична робота №7", 
    project_info="Створення найпростішого веб-додатку із використанням Flask.", 
    link="https://github.com/Prostokishyn/Practical7", 
    image="/static/project4.jpg", 
    project_tech="Python")

if __name__ == '__main__':
    app.run(debug=True)