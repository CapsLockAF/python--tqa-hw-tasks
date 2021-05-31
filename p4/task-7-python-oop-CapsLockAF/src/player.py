class Player:
    def __init__(self, name, age, height, weight):
        self.get_age = lambda: f"{name} is age {age}"
        self.get_height = lambda: f"{name} is {height}cm"
        self.get_weight = lambda: f"{name} weighs {weight}kg"
