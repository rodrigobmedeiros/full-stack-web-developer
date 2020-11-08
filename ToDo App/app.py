from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import sys

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://postgres:draGao01@localhost:5432/todoapp"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True

db = SQLAlchemy(app)
migrate = Migrate(app=app, db=db)

class Todo(db.Model):

    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)
    completed = db.Column(db.Boolean, nullable=False, default=False)


    def __repr__(self):

        return f'<Todo {self.id} {self.description}>'


@app.route('/')
def index():

    return render_template('index.html', data=Todo.query.order_by('id').all())

@app.route('/todos/<todo_id>', methods=['DELETE'])
def delete_task(todo_id):

    print(todo_id)
    try:
        todo = Todo.query.get(todo_id)
        db.session.delete(todo)
        db.session.commit()
    except:
        db.session.rollback()
    finally:
        db.session.close()

    return jsonify({'success': True})

@app.route('/todos/create', methods=['POST'])
def create_task():

    error = False
    body = {}
    try:
        description = request.get_json()['description']
        task = Todo(description=description)
        db.session.add(task)
        db.session.commit()
        body['description'] = task.description
    except:
        error = True
        db.session.rollback()
        print(sys.exc_info())
    finally:
        db.session.close()
    if not error:
        return jsonify(body)

@app.route('/todos/<todo_id>/set-completed', methods=['POST'])
def update_todos_status(todo_id):

    try:
        completed = request.get_json()['completed']
        todo = Todo.query.get(todo_id)
        print('completed', completed)
        todo.completed = completed
        db.session.commit()
    except:
        print('erro')
        db.session.rollback()
    finally:
        db.session.close()


    return redirect(url_for('index'))

if __name__ == '__main__':

    app.run()