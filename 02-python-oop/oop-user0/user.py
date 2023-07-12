class User :
    def __init__(self, first_name, last_name, email, age) :
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.gold_card_points = 0


    def display_info(self):
        print(f"User details : {self.gold_card_points}")


    def enroll(self, amount):
        self.gold_card_points = amount
        print(f"USER : {User.first_name}")
        return None

    def spend_points(self, amount):
        self.gold_card_points-=amount
        return None
    








john = User("John", "Mayer", "john@gmail.com", 35, 150)
alex = User("Alex", "Max","alex@gmail.com", 40, 200)