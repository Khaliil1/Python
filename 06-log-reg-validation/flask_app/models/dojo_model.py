from flask_app.config.mysqlconnection import connectToMySQL, flash
from flask_app import DB


class Dojo:
    def __init__(self, data_dict):
        self.id = data_dict["id"]
        self.name = data_dict["name"]
        self.dojo_location = data_dict["dojo_location"]
        self.fav_language = data_dict["fav_language"]
        self.comment = data_dict["comment"]
        self.created_at = data_dict["created_at"]
        self.updated_at = data_dict["updated_at"]

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojo;"
        results = connectToMySQL(DB).query_db(query)
        all_dojo = []
        print(results)
        for row in results:
            dojo = cls(row)
            all_dojo.append(dojo)
        return all_dojo

    @classmethod
    def create_dojo(cls, data_dict):
        query = """
                INSERT INTO dojo (name, dojo_location, fav_language, comment)
                VALUES(%(name)s, %(dojo_location)s, %(fav_language)s, %(comment)s);
                """

        result = connectToMySQL(DB).query_db(query, data_dict)
        print(result)
        return None

    @staticmethod
    def validate_dojo(dojo):
        is_valid = True  # we assume this is true
        if len(dojo["name"]) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(dojo["dojo_location"]):
            flash("Must choose a dojo location.")
            is_valid = False
        if int(dojo["fav_language"]):
            flash("Must choose a favorite language.")
            is_valid = False
        if len(dojo["comment"]) < 3:
            flash("Comments must be at least 3 characters.")
            is_valid = False
        return is_valid
