
from flask_restful import Resource, reqparse
from models.usermodel import UserModel


class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="Thise field is required!"
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="Thise field is required!"
                        )

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {'message': "User '{}' already exists!".format(data['username'])}, 400

        user = UserModel(**data)
        user.save_to_db()

        return {'message': 'User created successfully.'}, 201
