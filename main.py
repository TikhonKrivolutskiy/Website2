from flask import Flask, url_for, render_template
 
app = Flask(__name__)

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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')