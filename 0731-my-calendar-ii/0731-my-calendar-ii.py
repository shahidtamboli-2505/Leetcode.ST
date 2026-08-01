class MyCalendarTwo:

    def __init__(self):
        self.books = []
        self.overlaps = []

    def book(self, start: int, end: int) -> bool:
        # Triple booking check
        for s, e in self.overlaps:
            if max(start, s) < min(end, e):
                return False

        # Record new double bookings
        for s, e in self.books:
            if max(start, s) < min(end, e):
                self.overlaps.append((max(start, s), min(end, e)))

        # Add current booking
        self.books.append((start, end))
        return True