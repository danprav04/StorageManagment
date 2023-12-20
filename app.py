from flask import Flask, render_template, jsonify
import database as db
import format

app = Flask(__name__)


# API
@app.route('/api/get_users')
def get_users():
    users = format.users_to_dict(db.get_users())
    return jsonify(users)


# WEB PAGES
@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    app.run('0.0.0.0')
