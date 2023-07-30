
class Vehicle:
    def __init__(self, color, registration):
        self.color = color
        self.registration_number = registration


class Slot:
    def __init__(self, number):
        self.slot_number = number
        self.is_vacant = True
        self.vehicle = None

    def occupy(self, vehicle: Vehicle):
        self.is_vacant = False
        self.vehicle = vehicle

    def vacate(self):
        self.is_vacant = True
        self.vehicle = None


class Parking:
    _instance = None

    @classmethod
    def get_instance(cls, N):
        if cls._instance is None:
            cls._instance = cls(N)
        return cls._instance

    def __init__(self, N):
        self.N = N
        self.slots = [Slot(i+1) for i in range(self.N)]
        Parking.instance = self
        print(f"Created parking lot with {self.N} slots.")

    def park(self, registration, color):
        vehicle = Vehicle(registration, color)
        for slot in self.slots:
            if slot.is_vacant:
                slot.occupy(vehicle)
                print(f"Allocated slot number: {slot.slot_number}")
                return
        print("Sorry, Parking lot is full")

    def leave(self, slot_number):
        for slot in self.slots:
            if slot.slot_number == slot_number:
                slot.vacate()
                print(f"Slot number {slot.slot_number} is free")
                return
        # raise error
        print("Slot does not exist")

    def status(self):
        print("  Slot No.   " + " Registration No " + "  Color  ")
        for slot in self.slots:
            if not slot.is_vacant:
                print(
                    f"{slot.slot_number}   {slot.vehicle.registration_number}   {slot.vehicle.color}")
        return
