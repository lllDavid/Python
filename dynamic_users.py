class User:
    def __init__(self, id, username, email):
        self.id = id
        self.username = username
        self.email = email

    def __str__(self):
        return f"ID: {self.id} Username: {self.username} Email: {self.email}"

    @staticmethod
    def create_multiple(users: list):
        user_id = 1  
        for u in users:
            username = u.get("username")
            email = u.get("email")
            if username and email:
                user = User(user_id, username, email)  
                print(user)
                user_id += 1  

dict1 = [{"username": "Tom", "email": "tom@gmail.com"}, {"username": "Tim", "email": "tim@gmail.com"}]
User.create_multiple(dict1)