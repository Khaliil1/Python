from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash

import re  # the regex module

# create a regular expression object that we'll use later
EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$")


class User:
    def __init__(self, data_dict):
        self.id = data_dict["id"]
        self.email = data_dict["email"]
        self.created_at = data_dict["created_at"]
        self.updated_at = data_dict["updated_at"]

    @classmethod
    def create(cls, data_dict):
        query = """INSERT INTO users 
                    (email)
                    VALUES 
                    (%(email)s);"""
        return connectToMySQL(DATABASE).query_db(query, data_dict)

    @classmethod
    def get_by_id(cls, data_dict):
        query = """SELECT * FROM users WHERE id = %(id)s;"""
        result = connectToMySQL(DATABASE).query_db(query, data_dict)
        return cls(result[0])

    @classmethod
    def get_by_email(cls, data_dict):
        query = """SELECT * FROM users WHERE email = %(email)s;"""
        result = connectToMySQL(DATABASE).query_db(query, data_dict)
        if result:
            return cls(result[0])
        return False

    @staticmethod
    def validate_email(data_dict):
        is_valid = True
        if not EMAIL_REGEX.match(data_dict["email"]):
            flash("Email is not valid !!", "register")
            is_valid = False
        elif EMAIL_REGEX.match({"email": data_dict["email"]}):
            flash(
                "The email address you entered, is a valid email address! Thank you! ",
                "register",
            )
            is_valid = False
        return is_valid
