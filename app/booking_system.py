class HotelBookingSystem:
    def __init__(self):
        self.rooms = {
            "A1": True,
            "A2": True,
            "B1": True,
            "B2": True,
        }

    def check_availability(self, room_number):
        return self.rooms.get(room_number, None)

    def book_room(self, room_number):
        if room_number not in self.rooms:
            return "Room does not exist"

        if self.rooms[room_number] is False:
            return "Room already booked"

        self.rooms[room_number] = False
        return "Booking successful"

    def cancel_booking(self, room_number):
        if room_number not in self.rooms:
            return "Room does not exist"

        if self.rooms[room_number] is True:
            return "Room is not booked"

        self.rooms[room_number] = True
        return "Cancellation successful"
