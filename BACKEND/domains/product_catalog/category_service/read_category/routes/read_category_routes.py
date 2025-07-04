from flask import Blueprint
from read_category.controllers.read_category_controller import get_all_categories, get_category_by_id

read_category_bp = Blueprint('read_category_bp', __name__)

@read_category_bp.route('/categories', methods=['GET'])
def get_categories():
    return get_all_categories()

@read_category_bp.route('/categories/<int:category_id>', methods=['GET'])
def get_category(category_id):
    return get_category_by_id(category_id)
