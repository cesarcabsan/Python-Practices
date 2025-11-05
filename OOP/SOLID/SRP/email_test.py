class UserDB:
    def create_user(self, username, password, email):
        print("registered user in db")

class Email:
    def send_email(self, subject, to_email):
        print("email sent")

class ErrorLog:
    def log_error(self, error):
        print("log:", error)

class User:
    def register_user(self, username, password, email):
        try:
            user_db = UserDB()
            user_db.create_user(username, password, email)
            email_server = Email()
            email_server.send_email("User registered", email)
        except Exception:
            logger = ErrorLog()
            logger.log_error("error in user register")

user = User()
user.register_user("anji", "secret", "anji@example.com")

