from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def query(self, sql: str):
        pass

# Implementing Low level modules: Classes MySQL y MongoDB databases
class MySQLDatabase(Database):
    def query(self, sql: str):
        print(f"Executing MySQL Query: {sql}")

class MongoDBDatabase(Database):
    def query(self, sql: str):
        print(f"Executing MongoDB Query: {sql}")

# UserService that depends on the Database abstraction (High level module)
class UserService:
    def __init__(self, database: Database):
        self.database = database  

    def get_user(self, id: int):
        self.database.query(f"SELECT * FROM users WHERE id = {id}")

#Usage
mysql_db = MySQLDatabase()
user_service_mysql = UserService(mysql_db)
user_service_mysql.get_user(1)

mongo_db = MongoDBDatabase()
user_service_mongo = UserService(mongo_db)
user_service_mongo.get_user(2)
