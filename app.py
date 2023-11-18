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
    return render_template('index.html', days_of_the_week=days_arr)

if __name__ == "__main__":
    app.run(debug=True)