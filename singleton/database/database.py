from singleton import SingletonByArgs


class DatabaseClient(metaclass=SingletonByArgs):
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
    db3 = DatabaseClient("another")
    print(db1.connection)
    print(db2.connection)
    print(db3.connection)
    db1.add_classmate("Jão")
    db2.add_classmate("Jovana")
    db3.add_classmate("Tal")
    print(db1.classmates)
    print(db2.classmates)
    print(db3.classmates)
