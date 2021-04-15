from abc import abstractmethod

class Pet:
    def __init__(self, name):
        self.food_scale = 100
        self.toilet_scale = 100
        self.happiness_scale = 100
        self.is_ill = False
        self.is_walking = False
        self.name = name
    
    @abstractmethod
    def ask_for_food(self):
        raise NotImplementedError('i don\'t know how to speak')
    
    @abstractmethod
    def ask_for_toilet(self):
        raise NotImplementedError('i don\'t know how to speak')
    
    @abstractmethod
    def ask_for_happiness(self):
        raise NotImplementedError('i don\'t know how to speak')

class Dog(Pet):
    def __init__(self, name):
        super().__init__(name)
    
    def ask_for_food(self):
        return "Wuf! Where're bones, when I so need them?"
    
    def ask_for_toilet(self):
        return "Wuf! I don't think you want me to empty right here."
    
    def ask_for_happiness(self):
        return "Wuf! It's really boring to search for new entertainments in these 4 walls, can I chase any cats somewhere?"

class Cat(Pet):
    def __init__(self, name):
        super().__init__(name)

    def ask_for_food(self):
        return "Meow. Is there any sausage in this flat?"
    
    def ask_for_toilet(self):
        return "Meow. I don't think you want me to empty right here."
    
    def ask_for_happiness(self):
        return "Meow. I'd be very happy to play any game you suggest."