from flask import jsonify, request
from create_category.db.db import get_db

def get_all_categories():
    try:
        conn = get_db()
        cur = conn.cursor()
        cur.execute("SELECT id, name, description FROM categories;")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        categories = [
            {"id": row[0], "name": row[1], "description": row[2]}
            for row in rows
        ]
        return jsonify(categories), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def get_category_by_id(category_id):
    try:
        conn = get_db()
        cur = conn.cursor()
        cur.execute("SELECT id, name, description FROM categories WHERE id = %s;", (category_id,))
        row = cur.fetchone()
        cur.close()
        conn.close()
        if row:
            category = {"id": row[0], "name": row[1], "description": row[2]}
            return jsonify(category), 200
        else:
            return jsonify({"error": "Category not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
