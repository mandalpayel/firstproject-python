from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Define an empty list to store tasks
tasks = []

# Route to display the to-do list
@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

# Route to add a task
@app.route('/add', methods=['POST'])
def add_task():
    task = request.form['task']
    tasks.append(task)
    return redirect(url_for('index'))

# Route to mark a task as done
@app.route('/done/<int:task_id>')
def mark_done(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for('index'))

# Route to remove a task
@app.route('/remove/<int:task_id>')
def remove_task(task_id):
    if 0 <= task_id < len(tasks):
        removed_task = tasks.pop(task_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
