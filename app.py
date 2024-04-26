from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///newflask.db'
db = SQLAlchemy(app)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300), nullable=True)
    surname = db.Column(db.String(300), nullable=True)
    breed = db.Column(db.String(300), nullable=True)
    datе = db.Column(db.DateTime, nullable=True)
    comment = db.Column(db.Text, nullable=True)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        name = request.form['name']
        surname = request.form['surname']
        breed = request.form['breed']
        date = request.form['datе']
        comment = request.form['comment']
        post = Post(name=name, surname=surname, breed=breed, datе=date, comment=comment)
        try:
            db.session.add(post)
            db.session.commit()
            return redirect('/')
        except:
            print(name)
            print(surname)
            print(breed)
            print(date)
            print(comment)
            return 'Запись добалена'
    else:
        return render_template('create.html')


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
