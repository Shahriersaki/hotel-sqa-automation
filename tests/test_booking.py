from app.booking_system import HotelBookingSystem

def setup_function():
    global system
    system = HotelBookingSystem()

def test_room_available():
    assert system.check_availability("A1") is True

def test_successful_booking():
    result = system.book_room("A1")
    assert result == "Booking successful"
    assert system.check_availability("A1") is False

def test_double_booking():
    system.book_room("A2")
    result = system.book_room("A2")
    assert result == "Room already booked"

def test_cancel_booking():
    system.book_room("B1")
    result = system.cancel_booking("B1")
    assert result == "Cancellation successful"

def test_cancel_without_booking():
    result = system.cancel_booking("B2")
    assert result == "Room is not booked"

def test_invalid_room():
    result = system.book_room("Z9")
    assert result == "Room does not exist"
