from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory list to store todos
todos = []

@app.route('/')
def index():
    return render_template('devindex.html', todos=todos)

@app.route('/add', methods=['POST'])
def add():
    todo = request.form.get('todo')
    if todo:
        todos.append({'task': todo, 'done': False})
    return redirect(url_for('index'))

@app.route('/complete/<int:todo_id>')
def complete(todo_id):
    if 0 <= todo_id < len(todos):
        todos[todo_id]['done'] = True
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)

