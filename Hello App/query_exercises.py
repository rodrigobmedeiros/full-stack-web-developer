from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:draGao01@localhost:5432/app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)

    def __repr__(self):

        return f'<Person ID: {self.id}, name: {self.name}>'

db.create_all()

# user_1 = User(name='rodrigo')
# user_2 = User(name='renata')
# user_3 = User(name='adriane')
# user_4 = User(name='ariane')
# user_5 = User(name='isabella')

# db.session.add_all([user_1, user_2, user_3, user_4, user_5])
# db.session.commit()

# Test queries commands
print(User.query.filter(User.name.contains('rod')).all())