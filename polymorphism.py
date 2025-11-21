class Vehicle:
    def __init__(self, brand, merk):
        self.brand = brand
        self.merk = merk

    def move(self):
        print("Move!")

class Car(Vehicle):
    pass

class motor(Vehicle):
    def move(self):
        print("Fly!")

car1 = Car("Honda", "Avanza")
motor1 = motor("Yamaha", "Nmax")

for x  in (car1, motor1):
    print("================")
    print(x.brand)
    print(x.merk)
    x.move()
    print("================")
        