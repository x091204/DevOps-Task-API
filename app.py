from flask import Flask, render_template, request, redirect

app = Flask(__name__)

APP_NAME = "DevOps-Task-API"

tasks = []


@app.route("/")
def home():
    return render_template("index.html", tasks=tasks, app_name=APP_NAME)


@app.route("/add", methods=["POST"])
def add_task():
    task = request.form.get("task")

    if task:
        tasks.append({"task": task, "done": False})

    return redirect("/")


@app.route("/toggle/<int:index>")
def toggle_task(index):
    tasks[index]["done"] = not tasks[index]["done"]
    return redirect("/")


@app.route("/delete/<int:index>")
def delete_task(index):
    tasks.pop(index)
    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)