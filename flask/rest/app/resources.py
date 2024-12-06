from flask_restful import Resource, Api, reqparse, fields, marshal_with, abort
from app.models import UserModel
from app import db

# Defining request args for creating a user
user_args = reqparse.RequestParser()
user_args.add_argument('name', type=str, required=True, help="Name cannot be blank")
user_args.add_argument('email', type=str, required=True, help="Email cannot be blank")

# Defining request args for creating a user
user_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'email': fields.String
}

class Users(Resource):
    # Retrieves all the users
    @marshal_with(user_fields) 
    def get(self):
        users = UserModel.query.all()
        return users
    
    # Create a new user
    @marshal_with(user_fields)
    def post(self):
        args = user_args.parse_args()
        user = UserModel(name=args["name"], email=args["email"])
        db.session.add(user) 
        db.session.commit() 
        return user, 201    
    
class User(Resource):
    # Retrieves a user by their ID
    @marshal_with(user_fields)
    def get(self, id):
        user = UserModel.query.filter_by(id=id).first()
        if not user:
            abort(404, "User not found")
        return user
    
    # Updates a user record
    @marshal_with(user_fields)
    def put(self, id):
        args = user_args.parse_args()
        user = UserModel.query.filter_by(id=id).first()
        if not user:
            abort(404, "User not found")
        user.name = args["name"]
        user.email = args["email"]
        db.session.commit()
        return user
    
    # Deletes a user record
    @marshal_with(user_fields)
    def delete(self, id):
        user = UserModel.query.filter_by(id=id).first()
        if not user:
            abort(404, "User not found")

        db.session.delete(user)
        db.session.commit()
        return {'message': f"User(ID: {id}) deleted successfully"}, 204
