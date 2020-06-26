from flask_restful import Resource
from flask_restful import reqparse
from models.users import UserModel
from flask_jwt_extended import create_access_token, jwt_required, get_raw_jwt
from werkzeug.security import safe_str_cmp
from logoutlist import LOG_OUT_LIST

attribute = reqparse.RequestParser()
attribute.add_argument('login', type=str, required=True,
                       help="Field 'login' cannot be left blank")
attribute.add_argument('password', type=str, required=True,
                       help="Field 'password' cannot be left blank")


class User(Resource):
    # /users/
    @jwt_required
    def get(self, user_id):
        user = UserModel.find_user(user_id)
        if user:
            return user.parse_json()
        return {'message': 'User not found.'}, 404

    @jwt_required
    def delete(self, user_id):
        user = UserModel.find_user(user_id)
        if user:
            try:
                user.delete_user()
                return {'messsege': 'User Deleted.'}, 200
            except Exception as Error:
                return {
                           "message": "An internal error occurred trying to "
                                      "delete User. '{}'".format(
                               Error)}, 500
            # Internal Server Error
        return {'messsege': 'User not found.'}, 404


class UserRegister(Resource):
    # /register/
    def post(self):
        data = attribute.parse_args()
        if UserModel.find_by_login(data['login']):
            return {
                "message": "Login '{}' already exists.".format(data['login'])}
        user = UserModel(**data)
        user.save_user()
        return {'message': 'User created successfully'}, 201


class UserLogin(Resource):

    @classmethod
    def post(cls):
        data = attribute.parse_args()
        user = UserModel.find_by_login(data['login'])
        if user and safe_str_cmp(user.password, data['password']):
            token = create_access_token(identity=user.user_id)
            return {'acess_token': token}, 200
        return {'messege': "Username or Password is Wrong."}, 401


class UserLogout(Resource):

    @jwt_required
    def post(self):
        jwt_id = get_raw_jwt()['jti']  # Token Identifier
        LOG_OUT_LIST.add(jwt_id)
        return {'messege': 'Logged out successfully'}, 200
