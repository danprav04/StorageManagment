from flask import Flask, render_template, jsonify

app = Flask(__name__)


# API
@app.route('/api/test')
def hello_world():
    return jsonify({'response': 'success'})


@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    app.run('0.0.0.0')
