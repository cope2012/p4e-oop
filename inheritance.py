class Animal:
    def move(self):
        print('change position')

    def feed(self):
        print('needs to eat')


class Fish(Animal):
    def move(self):
        super().move()
        print('by swimming')


class Bird(Animal):
    def move(self):
        super().move()
        print('by flying')


dog = Animal()
dog.move()
dog.feed()
print("-----------")
fish = Fish()
fish.move()
fish.feed()
print("-----------")
bird = Bird()
bird.move()
bird.feed()
