from flask import Flask, url_for, render_template
 
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html', title='Готовимся к миссии')

@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', title='Тренировки в полёте', occ=prof.lower())   

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')