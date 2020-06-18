from flask import Flask
from flask_restful import Api
from resources.contacts import Contacts, Contact
from resources.users import User, UserRegister

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLAlchemy_TRACK_MODIFICATIONS'] = False
api = Api(app)


@app.before_first_request
def create_database():
    database.create_all()


api.add_resource(Contacts, '/contacts')
api.add_resource(Contact, '/contacts/<int:contact_id>')
api.add_resource(User, '/users/<int:user_id>')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    from sql_alchemy import database

    database.init_app(app)
    app.run(debug=True)
