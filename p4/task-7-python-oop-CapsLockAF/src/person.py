class Person:
    def __init__(self, person_name, love_food, hate_food):
        self.person_name = person_name
        self.love_food = love_food
        self.hate_food = hate_food

    def taste(self, food_name):
        name = self.person_name
        if food_name in self.love_food:
            return f"{name} eats the {food_name} and loves it!"
        elif food_name in self.hate_food:
            return f"{name} eats the {food_name} and hates it!"
        else:
            return f"{name} eats the {food_name}!"

