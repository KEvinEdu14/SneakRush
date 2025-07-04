from flask import request, jsonify
from create_category.db.db import get_db

def update_category(category_id):
    data = request.get_json()
    name = data.get('name')
    description = data.get('description', None)
    try:
        conn = get_db()
        cur = conn.cursor()
        cur.execute(
            "UPDATE categories SET name=%s, description=%s WHERE id=%s RETURNING id;",
            (name, description, category_id)
        )
        updated = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        if updated:
            return jsonify({"id": category_id, "name": name, "description": description}), 200
        else:
            return jsonify({"error": "Category not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
