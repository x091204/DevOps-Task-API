from flask import Flask, render_template, request, redirect
import pymysql
import os
import time

app = Flask(__name__)

APP_NAME = "DevOps-Task-API"

DB_CONFIG = {
    "host": os.getenv("MYSQL_HOST", "localhost"),
    "user": os.getenv("MYSQL_USER", "root"),
    "password": os.getenv("MYSQL_PASSWORD", "DevOps@123"),
    "database": os.getenv("MYSQL_DB", "tasksdb"),
    "cursorclass": pymysql.cursors.DictCursor,
    "unix_socket": "/var/lib/mysql/mysql.sock"
}


def get_db():
    return pymysql.connect(**DB_CONFIG)


def init_db():
    retries = 10
    while retries:
        try:
            conn = pymysql.connect(
                host=DB_CONFIG["host"],
                user=DB_CONFIG["user"],
                password=DB_CONFIG["password"],
                cursorclass=pymysql.cursors.DictCursor
            )
            with conn.cursor() as cursor:
                # Create database if not exists
                cursor.execute("CREATE DATABASE IF NOT EXISTS tasksdb")
                cursor.execute("USE tasksdb")
                # Create table if not exists
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS tasks (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        task VARCHAR(255) NOT NULL,
                        done BOOLEAN DEFAULT FALSE,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                """)
            conn.commit()
            conn.close()
            print("Database initialized successfully!")
            break
        except Exception as e:
            print(f"⏳ Waiting for MySQL... {retries} retries left. Error: {e}")
            retries -= 1
            time.sleep(3)


@app.route("/")
def home():
    conn = get_db()
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM tasks ORDER BY created_at DESC")
        tasks = cursor.fetchall()
    conn.close()
    return render_template("index.html", tasks=tasks, app_name=APP_NAME)


@app.route("/add", methods=["POST"])
def add_task():
    task = request.form.get("task")
    if task:
        conn = get_db()
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO tasks (task) VALUES (%s)", (task,))
        conn.commit()
        conn.close()
    return redirect("/")


@app.route("/toggle/<int:task_id>")
def toggle_task(task_id):
    conn = get_db()
    with conn.cursor() as cursor:
        cursor.execute("SELECT done FROM tasks WHERE id = %s", (task_id,))
        task = cursor.fetchone()
        if task:
            new_status = not task["done"]
            cursor.execute("UPDATE tasks SET done = %s WHERE id = %s", (new_status, task_id))
    conn.commit()
    conn.close()
    return redirect("/")


@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    conn = get_db()
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
    conn.commit()
    conn.close()
    return redirect("/")


if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000, debug=True)