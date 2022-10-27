from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Rono'}
    posts = [
        {
            'author': {'username': 'Guru'},
            'body': 'Welcome to Jujamaica!'
        },
        {
            'author': {'username': 'Mzushi'},
            'body': 'Tukibuya warazi wanagwaya!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
