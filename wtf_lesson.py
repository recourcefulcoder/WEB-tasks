from flask import Flask
from flask import redirect, url_for, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


class AccessForm(FlaskForm):
    part_name = StringField("Id астронавта", validators=[DataRequired()])
    part_pass = PasswordField('Пароль астронавта', validators=[DataRequired()])
    cap_name = StringField("Id капитана", validators=[DataRequired()])
    cap_pass = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Доступ')


@app.route('/')
def redir():
    return redirect("/login"
                    "")


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
    return render_template("auto_answer.html", **default_info)


@app.route("/login", methods=["POST", "GET"])
def solution():
    form = AccessForm()
    if form.validate_on_submit():
        return "Выполняется приказ"
    return render_template("login.html", form=form)


if __name__ == "__main__":
    app.run(port=8000)
