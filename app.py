from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db = SQLAlchemy(app)

app.app_context().push()

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(300), nullable=False)
    due_date = db.Column(db.String(25), nullable=False)
    is_complete = db.Column(db.Boolean, default=False)
    complete_date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return "<Todo %r>" % self.id

@app.route('/', methods=['POST', 'GET'])
def index():
    days_arr = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    if request.method == 'POST':
        task_content = request.form['content']
        task_due_date = request.form['due_date']
        new_task = Todo(content=task_content, due_date=task_due_date)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        
        except:
            return 'There was an error with submitting your task. Please try again later.'

    else:
        tasks = Todo.query.all()
        return render_template('index.html', days_of_the_week=days_arr, tasks=tasks)

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)
    
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    
    except:
        return 'There was an error with deleting your task. Please try again later.'

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    task = Todo.query.get_or_404(id)

    task.content = request.form['content']
    task.due_date = request.form['due_date']

    try:
        db.session.commit()
        return redirect('/')
    except:
        return "There was an issue with updating your task. Please try again later."

def complete():
    pass

def undo():
    pass

if __name__ == "__main__":
    app.run(debug=True)