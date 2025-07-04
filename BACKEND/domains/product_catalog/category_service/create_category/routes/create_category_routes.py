from flask import Blueprint
from create_category.controllers.create_category_controller import create_category

create_category_bp = Blueprint('create_category_bp', __name__)

@create_category_bp.route('/categories', methods=['POST'])
def add_category():
    return create_category()
