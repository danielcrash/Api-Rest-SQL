from flask import Flask, jsonify
from flask_restful import Api
from resources.contacts import Contacts, Contact
from resources.users import User, UserRegister, UserLogin, UserLogout
from flask_jwt_extended import JWTManager
from logoutlist import LOG_OUT_LIST

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLAlchemy_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'YourSecret'
app.config['JWT_BLACKLIST_ENABLED'] = True
api = Api(app)
jwt = JWTManager(app)


@app.before_first_request
def create_database():
    database.create_all()


@jwt.token_in_blacklist_loader
def check_log_out(token):
    return token['jti'] in LOG_OUT_LIST


@jwt.revoked_token_loader
def invalid_token():
    return jsonify({'messege': 'You already Logged out.'}), 401


api.add_resource(Contacts, '/contacts')
api.add_resource(Contact, '/contacts/<int:contact_id>')
api.add_resource(User, '/users/<int:user_id>')
api.add_resource(UserRegister, '/register')
api.add_resource(UserLogin, '/login')
api.add_resource(UserLogout, '/logout')

if __name__ == '__main__':
    from sql_alchemy import database

    database.init_app(app)
    app.run(debug=True)
