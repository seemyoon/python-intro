# Inheritance
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start(self):
        pass

    def stop(self):
        pass


class Car(Vehicle):
    def __init__(self, make, model, door_qty):
        super().__init__(make, model)
        self.door_qty = door_qty

    def lock_doors(self):
        pass

    def unlock_doors(self):
        pass
