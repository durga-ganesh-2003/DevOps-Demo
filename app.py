from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# In-memory list for todos (acting like temp DB)
todos = []

@app.route('/')
def index():
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add():
    todo = request.form.get('todo')
    if todo:
        todos.append({
            'task': todo,
            'done': False,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M')
        })
    return redirect(url_for('index'))

@app.route('/complete/<int:todo_id>')
def complete(todo_id):
    if 0 <= todo_id < len(todos):
        todos[todo_id]['done'] = True
    return redirect(url_for('index'))

@app.route('/delete/<int:todo_id>')
def delete(todo_id):
    if 0 <= todo_id < len(todos):
        todos.pop(todo_id)
    return redirect(url_for('index'))

@app.route('/edit/<int:todo_id>', methods=['POST'])
def edit(todo_id):
    updated_task = request.form.get('updated_task')
    if updated_task and 0 <= todo_id < len(todos):
        todos[todo_id]['task'] = updated_task
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)






