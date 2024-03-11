from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from flask import Flask, url_for, render_template
from wtforms import StringField, PasswordField, BooleanField, SubmitField


class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')

 
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html', title='Готовимся к миссии')

@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', title='Тренировки в полёте', occ=prof.lower())   

@app.route('/list_prof/<atr>')
def list_prof(atr):
    return render_template('list_prof.html', title='Список профессий', atr=atr)   

@app.route('/answer')
def answer():
    params = {}
    params['title'] = "Анкета"
    params['surname'] =  ""
    params['name'] = ""
    params['education'] = ""
    params['profession'] = ""
    params['gender'] = ""
    params['motivation'] = ""
    params['ready'] = ""
    return render_template('auto_answer.html', **params) 

@app.route('/auto_answer')
def auto_answer():
    params = {}
    params['title'] = "Анкета"
    params['surname'] =  "Watny"
    params['name'] = "Mark"
    params['education'] = "выше среднего"
    params['profession'] = "штурман марсохода"
    params['gender'] = "male"
    params['motivation'] = "Всегда мечтал застрять на Марсе!"
    params['ready'] = "True"
    return render_template('auto_answer.html', **params)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Аварийный доступ', form=form)

@app.route('/distribution')
def distribution():
    return render_template('distribution.html', title='По каютам!')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')