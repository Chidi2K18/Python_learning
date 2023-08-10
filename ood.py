import tests
class nat:
    # lets you define the parameters of the class
    def __init__(self, name, age, favourite_game, most_hours_game):
        self.name = name,
        self.age = age,
        self.favourite_game = favourite_game,
        self.most_hours_game = most_hours_game

    # this allows you to print the contents of the object once defined
    def __str__(self):
        return f"{self.name}{self.age}{self.favourite_game}{self.most_hours_game})"

    # this allows you to add a function into the class to do xyz
    def greeting(self):
        print("Hello my name is " + str(self.name))


# child class, remember child classes can inherit the functions and parameters of the parent class
#if you do an init function for the child it overrides the init from the parent
class childClass(nat):
    pass


# this is where you define the contents of the object
p1 = nat("NathaNael", 22, "Destiny", "RocketLeague")
p2 = childClass("test", 2, "life", "toy car")
#this is where you can call the methods of the class
print(p1)
p2.greeting()
#here I have imported a function from a different python file and called it
tests.captialCheck(str(p1.name))