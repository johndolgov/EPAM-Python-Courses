import abc
class Vehicle(metaclass=abc.ABCMeta):
    """Abstract class for any wehicle"""

    def __init__(self,year,model,wheels,quantity_of_miles):
        """Constructor"""

        self.year = year
        self.model = model
        self.wheels = wheels
        self.quantity_of_miles = quantity_of_miles

    @abc.abstractmethod
    def vehicle_type(self):
        """Vehicle type
        For Example Car,Motocycle etc
        """
        pass

    @abc.abstractmethod
    def is_motorcycle(self):
        pass

    @abc.abstractmethod
    def purchase_price(self):
        pass

class Car(Vehicle):
    """Wehicle - Car"""

    def __init__(self,year,model,wheels,quantity_of_miles):
        super().__init__(year,model,wheels,quantity_of_miles)

    def vehicle_type(self):
        return 'Car'

    def is_motorcycle(self):
        return wheels == 2

    def purchase_price(self):
        return 0.1*self.quantity_of_miles

class Motocycle(Vehicle):
    """Wehicle - Motocycle"""

    def __init__(self, year, model, wheels, quantity_of_miles):
        super().__init__(year, model, wheels, quantity_of_miles)

    def vehicle_type(self):
        return 'Motocycle'

    def is_motorcycle(self):
        return wheels == 2

    def purchase_price(self):
        return 0.1 * self.quantity_of_miles

class Truck(Vehicle):
    """Wehicle - Truck"""

    def __init__(self, year, model, wheels, quantity_of_miles):
        super().__init__(year, model, wheels, quantity_of_miles)

    def vehicle_type(self):
        return 'Truck'

    def is_motorcycle(self):
        return wheels == 2

    def purchase_price(self):
        return 0.1 * self.quantity_of_miles

class Bus(Vehicle):
    """Wehicle - Bus"""

    def __init__(self, year, model, wheels, quantity_of_miles):
        super().__init__(year, model, wheels, quantity_of_miles)

    def vehicle_type(self):
        return 'Bus'

    def is_motorcycle(self):
        return wheels == 2

    def purchase_price(self):
        return 0.1 * self.quantity_of_miles

if __name__ == '__main__':
    b = Bus(1998,'Pego',4,456)
    print(b.purchase_price())



