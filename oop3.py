from typing import override

class Rubberduck:
    color: str = "yellow"

    def __init__(self, quack_volume=5):
        self.__quack_volume = quack_volume

    @staticmethod
    def squeak():
        print('Squeaking')

    @classmethod
    def get_color(cls):
        return cls.color

    def boost_volume(self):
        self.__quack_volume += 1

    @property
    def quack_volume(self):
        return self.__quack_volume

    @quack_volume.setter
    def quack_volume(self, quack_volume):
        if quack_volume >= 0:
            self.__quack_volume = quack_volume

    def __str__(self):
        return f"Rubberduck's color: {self.color}, volume: {self.__quack_volume}"


duck = Rubberduck()
print(duck)

Rubberduck.squeak()

duck.quack_volume = 10
print("🔊 New volume:", duck.quack_volume)

duck.boost_volume()
print("🚀 Boosted volume:", duck.quack_volume)

print("🎨 Default color:", Rubberduck.get_color())

