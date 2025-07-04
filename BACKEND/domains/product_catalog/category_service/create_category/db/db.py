import psycopg2
import os

def get_db():
    return psycopg2.connect(
        host=os.getenv('DB_HOST', 'postgres'),
        port=os.getenv('DB_PORT', 5432),
        user=os.getenv('DB_USER', 'sneakrush'),
        password=os.getenv('DB_PASSWORD', 'sneakrushpass'),
        dbname=os.getenv('DB_NAME', 'sneakrushdb')
    )
