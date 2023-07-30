from app.model import Parking


if __name__ == '__main__':

    ch = "Y"
    ParkingLot = None

    while ch != "N":
        command = input()
        key, *values = command.split(" ")
        if key == "create_parking_lot":
            ParkingLot = Parking(int(values[0]))
        elif key == "park":
            ParkingLot.park(values[0], values[1])
        elif key == "leave":
            try:
                slot_number = int(values[0])
                ParkingLot.leave(slot_number)
            except ValueError:
                print("Invalid slot number. Please enter a valid integer.")

        elif key == "status":
            ParkingLot.status()

        ch = input("Press any key for new command, N to exit")
