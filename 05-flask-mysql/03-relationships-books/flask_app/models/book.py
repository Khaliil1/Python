from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE_NAME

class Book:
    def __init__(self, data_dict):
        self.id = data_dict["id"]
        self.tittle = data_dict["tittle"]
        self.num_of_pages = data_dict["num_of_pages"]
        self.created_at = data_dict["created_at"]
        self.updated_at = data_dict["updated_at"]


    @classmethod
    def get_all(cls):
        query = """ SELECT * FROM authors; """

        result = connectToMySQL(DATABASE_NAME).query_db(query)

        all_books = []
        for row in result:
            book = cls(row)
            all_books.append(book)
        return all_books
    
    @classmethod
    def create(cls, date_dict):
        query = """INSERT INTO books (author_id, tittle, pages, release_year) 
                VALUE (%(author_id)s, %(tittle)s, %(pages)s, %(release_year)s);"""
        result = connectToMySQL(DATABASE_NAME).query_db(query, date_dict)
        return result