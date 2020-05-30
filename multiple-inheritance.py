class Animal:
    def move(self):
        print('Animal move called')
        print('change position')

    def feed(self):
        print('needs to eat')


class Fish(Animal):
    def move(self):
        print('Fish move called')
        super().move()
        print('by swimming')


class Bird(Animal):
    def move(self):
        print('Bird move called')
        super().move()
        print('by flying')


class SwimmingBird(Bird, Fish):
    def move(self):
        print('SwimmingBird move called')
        super().move()


# dog = Animal()
# dog.move()
# print("-----------")
# fish = Fish()
# fish.move()
# fish.feed()
# print("-----------")
# bird = Bird()
# bird.move()
# bird.feed()
# print("-----------")
duck = SwimmingBird()
duck.move()
duck.feed()
