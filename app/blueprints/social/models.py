from app import db, login
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    id= db.Column(db.Integer, primary_key=True)
    username= db.Column(db.String(64), unique=True, nullable=False)
    email= db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    blogs= db.relationship('Blog', backref='narrator', lazy='dynamic')
    pokemons= db.relationship('Pokemon', backref='collector', lazy='dynamic')


    def __repr__(self):
        return f'<User: {self.username}>'
    
    def hash_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def commit(self):
        db.session.add(self)
        db.session.commit()

    
class Blog(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    blogblock = db.Column(db.String(250))
    user_id= db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Blogs: {self.blogblock}>'
    
    def commit(self):
        db.session.add(self)
        db.session.commit()

class Pokemon(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    pokemon_name= db.Column(db.String(100), unique=True, nullable=False)
    ability=db.Column(db.String(150), nullable=False)
    type= db.Column(db.String(150),nullable=False )
    sprite=db.Column(db.String(250), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    user_id= db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self,pokemon_name,ability,type,sprite,user_id):
        self.pokemon_name=pokemon_name
        self.ability=ability
        self.type=type
        self.sprite=sprite
        self.user_id=user_id

    # def known_pokemon(pokemon_name):
    #     return Pokemon.query.filter_by(pokemon_name=pokemon_name).first()

    def commit(self):
        db.session.add(self)
        db.session.commit()

    # def delete_pokemon(self):
    #     db.session.delete(self)
    #     db.session.commit()