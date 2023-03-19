
class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class SingletonByArgs(type):
    """"""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        key = (cls, *args)
        if key not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[key] = instance
        return cls._instances[key]