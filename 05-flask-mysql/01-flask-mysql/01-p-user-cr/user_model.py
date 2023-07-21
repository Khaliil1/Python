from mysqlconnection import connectToMySQL
class User :
    def __init__(self, data_dict) :
        self.id = data_dict['id']
        self.first_name = data_dict['first_name']
        self.last_name = data_dict['last_name']
        self.email = data_dict['email']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']


    # ! all query must be in class methods
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM artist;"
        results = connectToMySQL("user_schema").query_db(query)
        all_user=[]
        print(results)
        for row in results:
            user = cls(row)
            all_user.append(user)
        return all_user


    @classmethod
    def create_artist(cls, data_dict):
        query = """
                INSERT INTO artist (first_name, last_name, email)
                VALUES(%(first_name)s, %(last_name)s, %(email)s);
                """
        
        result = connectToMySQL("user_schema").query_db(query, data_dict)
        print(result)
        return None