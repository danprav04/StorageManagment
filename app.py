from flask import Flask, render_template, jsonify
import database as db

app = Flask(__name__)


# API
@app.route('/api/get_users')
def test():
    users = db.get_users()
    return jsonify(users)


# WEB PAGES
@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    app.run('0.0.0.0')
