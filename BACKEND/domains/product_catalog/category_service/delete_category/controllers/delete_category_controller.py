from flask import jsonify
from create_category.db.db import get_db

def delete_category(category_id):
    try:
        conn = get_db()
        cur = conn.cursor()
        cur.execute("DELETE FROM categories WHERE id = %s RETURNING id;", (category_id,))
        deleted = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        if deleted:
            return jsonify({"message": "Category deleted"}), 200
        else:
            return jsonify({"error": "Category not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
