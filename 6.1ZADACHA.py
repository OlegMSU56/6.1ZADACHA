class Plant:
    edible = False

    def __init__(self, name):
        self.name = name


class Flower(Plant):
    pass


class Fruit(Plant):
    edible = True


class Animal:
    alive = True
    fed = False

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        if food.edible == True:
            Animal.fed = True
            print(f'{self.name} съел {food.name}')
        if food.edible == False:
            Animal.alive = False
            print(f'{self.name} не стал есть {food.name}')


class Mammal(Animal):
    pass


class Predator(Animal):
    pass


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(f'{a1.name} жив: {a1.alive}')
print(f'{a2.name} сытый: {a2.fed}')
a1.eat(p1)
a2.eat(p2)
print(f'{a1.name} жив: {a1.alive}')
print(f'{a2.name} сытый: {a2.fed}')
