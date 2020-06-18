from flask_restful import Resource
from flask_restful import reqparse
from models.users import UserModel


class User(Resource):
    # /users/
    def get(self, user_id):
        user = UserModel.find_user(user_id)
        if user:
            return user.parse_json()
        return {'message': 'User not found.'}, 404

    def delete(self, user_id):
        user = UserModel.find_user(user_id)
        if user:
            try:
                user.delete_user()
                return {'messsege': 'User Deleted.'}, 200
            except Exception as Error:
                return {"message": "An internal error occurred trying to delete User. '{}'".format(Error)}, 500
            # Internal Server Error
        return {'messsege': 'User not found.'}, 404


class UserRegister(Resource):
    # /register/
    def post(self):
        attribute = reqparse.RequestParser()
        attribute.add_argument('login', type=str, required=True, help="Field 'login' cannot be left blank")
        attribute.add_argument('password', type=str, required=True, help="Field 'password' cannot be left blank")
        data = attribute.parse_args()

        if UserModel.find_by_login(data['login']):
            return {"message": "Login '{}' already exists.".format(data['login'])}
        user = UserModel(**data)
        user.save_user()
        return {'message': 'User created successfully'}, 201
