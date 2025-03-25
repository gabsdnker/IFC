class Singleton:
    _instance = None #Atributo estático para armazenar a única iinstância

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

obj1 = Singleton()
obj2 = Singleton()

print(obj1 is obj2)
