from flask import Flask
from flask import redirect
from flask import url_for
from flask import render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def redir():
    return redirect("/Заголовок")


@app.route("/<title>")
@app.route("/index/<title>")
def main_page(title):
    return render_template("base.html", title=title)


@app.route("/training/<string:profession>")
def training(profession):
    params = {
        "title": "Тренировка",
        "prof": profession,
        "way_to_static": url_for("static", filename="img")
    }
    return render_template("training.html", **params)


@app.route("/list_prof/<string:request_type>")
def list_prof(request_type):
    params = {
        "type": request_type,
        "title": "Список профессий",
    }
    return render_template("list_prof.html", **params)


@app.route("/auto_answer")
@app.route("/answer")
def auto_answer():
    default_info = {
        "title": "Анкета",
        "surname": "Кириенко",
        "name": "Георгий",
        "education": "Высшее",
        "profession": "Программист",
        "sex": "male",
        "motivation": "А почему бы и нет)",
        "ready": True
    }
    return render_template("auto_answer.html", info=default_info, title=default_info["title"])


if __name__ == "__main__":
    app.run(port=8000)
