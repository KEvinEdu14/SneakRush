from flask import request, jsonify
from create_category.models.category_model import Category
from create_category.db.db import get_db

def create_category():
    data = request.get_json()
    name = data.get('name')
    description = data.get('description', None)
    category = Category(name, description)
    try:
        conn = get_db()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO categories (name, description) VALUES (%s, %s) RETURNING id;",
            (category.name, category.description)
        )
        category_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({"id": category_id, "name": category.name, "description": category.description}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
