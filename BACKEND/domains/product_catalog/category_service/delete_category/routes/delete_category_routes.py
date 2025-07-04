from flask import Blueprint
from delete_category.controllers.delete_category_controller import delete_category

delete_category_bp = Blueprint('delete_category_bp', __name__)

@delete_category_bp.route('/categories/<int:category_id>', methods=['DELETE'])
def delete_category_route(category_id):
    return delete_category(category_id)
