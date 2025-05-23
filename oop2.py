from typing import override

class Customer:
    def __init__(self, name, email, id):
        self.name = name
        self.email = email
        self.__id = id

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        if value >= 0:
            self.__id = value

    @override
    def __str__(self):
        return f"Customer's Name: {self.name}, (ID: {self.id}), Email address:{self.email}"

    @override
    def __repr__(self):
        return f"Customer('Name = {self.name}', 'Email = {self.email}',ID = {self.id})"

c1 = Customer("Daniel", "Daniel1899@example.com", 100)
c2 = Customer("Ella", "Ella2011@example.com", 4)

print(c1)
print(repr(c2))
