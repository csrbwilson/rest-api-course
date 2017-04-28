from flask import Flask
from flask_jwt import JWT
from flask_restful import Api

from section008.resources.item import ItemList, Item
from section008.resources.store import StoreList, Store
from section008.resources.user import UserRegister
from section008.security import authenticate, identity

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'hero'
api = Api(app)

jwt = JWT(app, authenticate, identity) # creates new endpoint /auth

# @app.before_request
# def before_request():
#     if True:
#         print("HEADERS", request.headers)
#         print("REQ_path", request.path)
#         print("ARGS",request.args)
#         print("DATA",request.data)
#         print("FORM",request.form)

api.add_resource(Item, '/item/<string:name>')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    from section008.db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
