#https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/
#>>> from app import db
#>>> db.create_all()
from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "cisco"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///d.db'
#Valid SQLite URL forms are:
#sqlite:///:memory: (or, sqlite://)
#sqlite:///relative/path/to/file.db
#sqlite:////absolute/path/to/file.db
db = SQLAlchemy(app)

class U(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)


@app.route('/')
def index():
    users = U.query.all()
    return render_template('home.html', user_list=users)

@app.route('/insert')
def insert():
    username = request.args.get('fname')
    name = U(name=username)
    db.session.add(name)
    db.session.commit()
    return redirect("http://127.0.0.1:5000/")

@app.route('/update')
def update():
    id = request.args.get('id')
    user = U.query.filter_by(id=id).first()

    if 'fname' in request.args:
        user = U.query.filter_by(name=session["name"]).first()
        user.name = request.args.get('fname')
        db.session.commit()
        return redirect("http://127.0.0.1:5000/")
    else:
        session["name"] = user.name
        return render_template('update.html', user=user.name)    


if __name__ == '__main__':
    app.run()
