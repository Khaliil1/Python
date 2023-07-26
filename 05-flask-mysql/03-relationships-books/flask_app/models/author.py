from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE_NAME
class Author:

    def __init__(self, data_dict):
        self.name = data_dict["name"]
        self.nationality = data_dict["nationality"]
        self.created_at = data_dict["created_at"]
        self.updated_at = data_dict["updated_at"]
        

    @classmethod
    def get_all(cls):
        query = """ SELECT * FROM authors; """
        query_2 = """SELECT * FROM authors
                                JOIN books ON authors.id = books.authors.id;"""
        results = connectToMySQL(DATABASE_NAME).query_db(query_2)

        all_authors = []
        for row in results:
            author = cls(row)
            all_authors.append(author)
        return all_authors
    
    @classmethod
    def create(cls, date_dict):
        query = """INSERT INTO authors (name, nationality) VALUE (%(name)s, %(nationality)s);"""
        result = connectToMySQL(DATABASE_NAME).query_db(query, date_dict)
        return