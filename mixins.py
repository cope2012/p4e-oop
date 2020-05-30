class Animal:
    def move(self):
        print('change position')

    def feed(self):
        print('needs to eat')


class CanSwim:
    def can_swim(self):
        print('by swimming')


class CanFly:
    def can_fly(self):
        print('by flying')


class Fish(Animal, CanSwim):
    def move(self):
        super().move()
        self.can_swim()


class Bird(Animal, CanFly):
    def move(self):
        super().move()
        self.can_fly()


class SwimmingBird(Bird, CanSwim):
    def move(self):
        super().move()
        self.can_swim()


dog = Animal()
dog.move()
print("-----------")
fish = Fish()
fish.move()
fish.feed()
print("-----------")
bird = Bird()
bird.move()
bird.feed()
print("-----------")
duck = SwimmingBird()
duck.move()
duck.feed()
