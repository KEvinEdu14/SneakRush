from flask import Blueprint
from update_category.controllers.update_category_controller import update_category

update_category_bp = Blueprint('update_category_bp', __name__)

@update_category_bp.route('/categories/<int:category_id>', methods=['PUT'])
def update_category_route(category_id):
    return update_category(category_id)
