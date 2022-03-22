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


if __name__ == "__main__":
    app.run(port=8000)
