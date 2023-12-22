from flask import Flask, render_template, jsonify, request
import database as db
import format

app = Flask(__name__)
api_path = '/api'


# API
@app.route(f'{api_path}/get_users')
def get_users():
    users = format.users_to_dict(db.get_users())
    return jsonify(users)


@app.route(f'{api_path}/get_storage_places')
def get_storage_places():
    storage_places = format.storage_places_to_dict(db.get_storage_places())
    return jsonify(storage_places)


@app.route(f'{api_path}/get_storage_grids')
def get_storage_grids():
    storage_grids = format.storage_grids_to_dict(db.get_storage_grids())
    return jsonify(storage_grids)


@app.route(f'{api_path}/get_storage_units')
def get_storage_units():
    storage_units = format.storage_units_to_dict(db.get_storage_units())
    return jsonify(storage_units)


@app.route(f'{api_path}/create_storage_place', methods=['POST'])
def create_storage_place():
    try:
        data = request.get_json()
        name = data.get('name')
        description = data.get('description')
        image = data.get('image')

        if not all([name, description, image]):
            return jsonify({'error': 'Missing required parameters'}), 400

        result = db.create_storage_place(name=name, description=description, image=image)
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route(f'{api_path}/create_storage_grid', methods=['POST'])
def create_storage_grid():
    try:
        data = request.get_json()
        name = data.get('name')
        description = data.get('description')
        row_count = data.get('row_count')
        column_count = data.get('column_count')
        image = data.get('image')
        storage_place_id = data.get('storage_place_id')

        if not all([name, description, row_count, column_count, image, storage_place_id]):
            return jsonify({'error': 'Missing required parameters'}), 400

        result = db.create_storage_grid(
            name=name,
            description=description,
            row_count=row_count,
            column_count=column_count,
            image=image,
            storage_place_id=storage_place_id,
        )
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route(f'{api_path}/create_storage_unit', methods=['POST'])
def create_storage_unit():
    try:
        data = request.get_json()
        name = data.get('name')
        description = data.get('description')
        image = data.get('image')
        storage_place_id = data.get('storage_place_id')
        storage_grid_id = data.get('storage_grid_id')
        storage_grid_row = data.get('storage_grid_row')
        storage_grid_column = data.get('storage_grid_column')

        if not all([name, description, image, storage_place_id, storage_grid_id, storage_grid_row, storage_grid_column]):
            return jsonify({'error': 'Missing required parameters'}), 400

        result = db.create_storage_unit(
            name=name,
            description=description,
            image=image,
            storage_place_id=storage_place_id,
            storage_grid_id=storage_grid_id,
            storage_grid_row=storage_grid_row,
            storage_grid_column=storage_grid_column,
        )
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# WEB PAGES
@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    app.run('0.0.0.0')
