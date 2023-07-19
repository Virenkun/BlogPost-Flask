class User:
    def __init__(self, username, email, image_file, password):
        self.username = username
        self.email = email
        self.image_file = image_file
        self.password = password


class Post:
    def __init__(self, title, date_posted, content, user_id):
        self.title = title
        self.date_posted = date_posted
        self.content = content
        self.user_id = user_id
