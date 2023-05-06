from flask import Flask, jsonify, request, make_response
import sqlite3
import config as cf
app = Flask(__name__)

# route to retrieve all items
@app.route('/characters', methods=['GET'])
def get_items():
    try:
        conn = sqlite3.connect(cf.db_name)
        cur = conn.cursor()
        cur.execute(f'SELECT * FROM {cf.table_name}')
        items = cur.fetchall()
        conn.close()
        return jsonify(items)
    except Exception as e:
        return make_response(str(e), 500)

# route to retrieve a single item by id
@app.route('/characters/<int:item_id>', methods=['GET'])
def get_item(item_id):
    try:
        conn = sqlite3.connect(cf.db_name)
        cur = conn.cursor()
        cur.execute(f'SELECT * FROM {cf.table_name} WHERE id = {item_id}')
        item = cur.fetchone()
        conn.close()
        if item:
            return jsonify(item)
        else:
            return make_response('Item not found', 404)
    except Exception as e:
        return make_response(str(e), 500)

# # route to create a new item
# @app.route('/items', methods=['POST'])
# def create_item():
#     try:
#         data = request.get_json()
#         conn = sqlite3.connect(db_name)
#         cur = conn.cursor()
#         cur.execute('INSERT INTO items (name, description, price) VALUES (?, ?, ?)', (data['name'], data['description'], data['price']))
#         item_id = cur.lastrowid
#         conn.commit()
#         conn.close()
#         return jsonify({'id': item_id}), 201
#     except Exception as e:
#         return make_response(str(e), 500)

# # route to update an existing item
# @app.route('/items/<int:item_id>', methods=['PUT'])
# def update_item(item_id):
#     try:
#         data = request.get_json()
#         conn = sqlite3.connect(db_name)
#         cur = conn.cursor()
#         cur.execute('UPDATE items SET name = ?, description = ?, price = ? WHERE id = ?', (data['name'], data['description'], data['price'], item_id))
#         conn.commit()
#         conn.close()
#         return '', 204
#     except Exception as e:
#         return make_response(str(e), 500)

# # route to delete an item by id
# @app.route('/items/<int:item_id>', methods=['DELETE'])
# def delete_item(item_id):
#     try:
#         conn = sqlite3.connect('example.db')
#         cur = conn.cursor()
#         cur.execute('DELETE FROM items WHERE id = ?', (item_id,))
#         conn.commit()
#         conn.close()
#         return '', 204
#     except Exception as e:
#         return make_response(str(e), 500)

if __name__ == '__main__':
    app.run(debug=True)
