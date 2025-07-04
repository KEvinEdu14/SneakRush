from flask import Flask
from create_category.routes.create_category_routes import create_category_bp
from read_category.routes.read_category_routes import read_category_bp
from update_category.routes.update_category_routes import update_category_bp
from delete_category.routes.delete_category_routes import delete_category_bp
app = Flask(__name__)
app.register_blueprint(create_category_bp)
app.register_blueprint(read_category_bp)
app.register_blueprint(update_category_bp)
app.register_blueprint(delete_category_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
