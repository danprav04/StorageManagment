from flask import Flask, render_template, jsonify, request
import database as db
import format

app = Flask(__name__)


# API
@app.route('/api/get_users')
def get_users():
    users = format.users_to_dict(db.get_users())
    return jsonify(users)


@app.route('/api/get_storage_places')
def get_storage_places():
    storage_places = format.storage_places_to_dict(db.get_storage_places())
    return jsonify(storage_places)


@app.route('/api/create_storage_place', methods=['POST'])
def create_storage_place():
    try:
        data = request.get_json()
        name = data.get('name')
        description = data.get('description')
        image = data.get('image')

        if not all([name, description, image]):
            return jsonify({'error': 'Missing required parameters'}), 400

        result = create_storage_place(name=name, description=description, image=image)
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# WEB PAGES
@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    app.run('0.0.0.0')
