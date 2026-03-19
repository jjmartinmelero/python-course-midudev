
class Car:

    # attr class
    type = "car with four wheel"

    # constructor
    def __init__(self, model, color):
        # attr instance
        self.model = model
        self.color = color

    def start_car(self):
        print(f"{self.model} started !")


car1 = Car("Toyota Corolla", "red")
car2 = Car("Kia Ceed", "blue")

car2.start_car()
