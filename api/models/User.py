from api.core.application import bcrypt
from api.core.database import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def json(self):
        return {
            'id': self.id,
            'email': self.email,
            'password': self.password
        }

    def get_user_by_email(email):
        user = User.query.filter_by(email=email).first()
        if user is not None:
            return user
    
    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)
    
    def get_all_users():
        users = User.query.all()
        if users is not None:
            return users 
        # return [User.json(user) for user in User.query.all()]
    
