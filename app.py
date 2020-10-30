from flask import Flask, render_template, request, redirect
import app_db_operations as dboperations

app = Flask(__name__)

@app.route('/')
def index():
    users = dboperations.get_users()
    return render_template('home.html', user_list=users)

@app.route('/insert')
def insert():
    username = request.args.get('fname') #learn usermane from URL
    dboperations.insert_user(username) #insert username to db
    return redirect("http://127.0.0.1:5000/")


if __name__ == '__main__':
    app.run()
