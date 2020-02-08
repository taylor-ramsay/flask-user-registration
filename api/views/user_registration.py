from flask import request, jsonify

from api.core.application import application
from api.core.database import db
from api.models.User import User
from api.core.application import bcrypt


@application.route("/register", methods=["POST"])
def register():
    email = request.json["email"]
    password = request.json["password"]
    verify_password = request.json["verify_password"]
    if password != verify_password:
        return jsonify({"msg": "Passwords don't match."}), 400
    if not email or not password or not verify_password:
        return jsonify({"msg": "Form is incomplete."}), 400
    db_user = User.get_user_by_email(email)
    if db_user is not None:
        return jsonify({"msg": "This email is already registered"}), 400
    pw_hash = bcrypt.generate_password_hash(password).decode('utf-8')
    db.session.add(User(email=email, password=pw_hash))
    db.session.commit()
    created_user = User.get_user_by_email(email)
    return jsonify({'user': User.json(created_user)})


@application.route("/login", methods=["POST"])
def login():
    email = request.json["email"]
    print('email:', email)
    password = request.json["password"]
    if not email or not password:
        return jsonify({"msg": "Email or password is missing"}), 400
    db_user = User.get_user_by_email(email)
    print('db_user:', db_user)
    if db_user is not None and db_user.check_password(password):
        return jsonify({"msg": "Logged in!"}), 200
    return jsonify({"msg": "Incorrect username or password"}), 400


