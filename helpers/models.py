from datetime import datetime
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash

# Assuming you're using MongoDB locally
client = MongoClient("mongodb://localhost:27017/")  # Adjust the connection string as needed
db = client["fleet_management_system"]  # Database name
users_collection = db["users"]  # Collection name for users

class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password_hash = generate_password_hash(password)  # Hash the password before storing
        self.created_at = datetime.utcnow()  # Store the time when the user is created

    def save(self):
        """ Save the user to the MongoDB database """
        user_data = {
            "username": self.username,
            "email": self.email,
            "password_hash": self.password_hash,
            "created_at": self.created_at
        }
        # Insert the user data into the collection
        users_collection.insert_one(user_data)

    @classmethod
    def get_by_email(cls, email):
        """ Fetch user from the database by email """
        user_data = users_collection.find_one({"email": email})
        if user_data:
            return cls(user_data["username"], user_data["email"], user_data["password_hash"])
        return None

    @classmethod
    def get_by_username(cls, username):
        """ Fetch user from the database by username """
        user_data = users_collection.find_one({"username": username})
        if user_data:
            return cls(user_data["username"], user_data["email"], user_data["password_hash"])
        return None

    def check_password(self, password):
        """ Check if the provided password matches the hashed password """
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        """ Convert the User object to a dictionary """
        return {
            "username": self.username,
            "email": self.email,
            "created_at": self.created_at
        }
