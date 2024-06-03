import sqlite3
import os
from FDataBase import FDataBase
from flask import Flask, render_template, request, g, flash, abort, url_for

DEBUG = True
SECRET_KEY = 'IDFKAiddqd123!@%'

app = Flask(__name__)

app.config.from_object(__name__)

app.config.update(dict(DATABASE=os.path.join(app.root_path, 'app.db')))

def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn

def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()

def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db

dbase = None
@app.before_request
def before_request():
    """Установление соединения с БД перед выполнением запроса"""
    global dbase
    db = get_db()
    dbase = FDataBase(db)

@app.route("/")
def index():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('index.html', menu = dbase.getMenu())

@app.route("/longreads")
def longreads():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('longreads.html', menu = dbase.getMenu())

@app.route("/udmCities")
def udmCities():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('udmCities.html', menu = dbase.getMenu())


@app.route("/tests")
def tests():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('tests.html', menu = dbase.getMenu())

@app.route("/about")
def about():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('about.html', menu = dbase.getMenu())

@app.route("/health")
def health():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('health.html', menu = dbase.getMenu())

@app.route("/psycho")
def psycho():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('psycho.html', menu = dbase.getMenu())

@app.route("/fashion")
def fashion():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('fashion.html', menu = dbase.getMenu())

@app.route("/dietas")
def dietas():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('dieta.html', menu = dbase.getMenu())

@app.route("/women_products")
def women_products():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('women_products.html', menu = dbase.getMenu())

@app.route("/zebras")
def zebras():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('zebras.html', menu = dbase.getMenu())

@app.route("/author_collumns")
def author_collumns():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('author_collumns.html', menu = dbase.getMenu())

@app.route("/reportages")
def reportages():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('reportages.html', menu = dbase.getMenu())

@app.teardown_appcontext
def close_db(error):
    '''Закрываем соединение с БД, если оно было установлено'''
    if hasattr(g, 'link_db'):
        g.link_db.close


@app.errorhandler(404)
def PageNotFound(error):
    return render_template('page404.html', title="Страница не найдена")

if __name__ == "__main__":
        app.run(debug=True)

