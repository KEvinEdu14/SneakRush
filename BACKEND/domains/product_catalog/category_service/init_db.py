import psycopg2
import os
import time

def wait_for_postgres():
    while True:
        try:
            conn = psycopg2.connect(
                host=os.getenv('DB_HOST', 'postgres'),
                port=os.getenv('DB_PORT', 5432),
                user=os.getenv('DB_USER', 'sneakrush'),
                password=os.getenv('DB_PASSWORD', 'sneakrushpass'),
                dbname=os.getenv('DB_NAME', 'sneakrushdb')
            )
            conn.close()
            break
        except Exception as e:
            print("Esperando a que PostgreSQL esté listo...", str(e))
            time.sleep(2)

def init_db():
    wait_for_postgres()
    conn = psycopg2.connect(
        host=os.getenv('DB_HOST', 'postgres'),
        port=os.getenv('DB_PORT', 5432),
        user=os.getenv('DB_USER', 'sneakrush'),
        password=os.getenv('DB_PASSWORD', 'sneakrushpass'),
        dbname=os.getenv('DB_NAME', 'sneakrushdb')
    )
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS categories (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        description TEXT
    );
    """)
    conn.commit()
    cur.close()
    conn.close()
    print("Tabla 'categories' verificada o creada.")

if __name__ == '__main__':
    init_db()
