from singleton import Singleton


class DatabaseClient(metaclass=Singleton):
    """classmates database on RAM"""
    connection = 0

    def __init__(self, connection_url):
        self.connection = connection_url
        self.__classmates = []

    def add_classmate(self, classmate):
        self.classmates.append(classmate)

    @property
    def classmates(self):
        return self.__classmates


if __name__ == "__main__":
    same_connection = "postgresql://localhost:5432"
    db1 = DatabaseClient(same_connection)
    db2 = DatabaseClient(same_connection)
    print(db1.connection)
    print(db2.connection)
    if db1 == db2:
        print("same db connection")
    else:
        print("different database connection")

    db1.add_classmate("Jão")
    db2.add_classmate("Jovana")
    print(db1.classmates)
    print(db2.classmates)

